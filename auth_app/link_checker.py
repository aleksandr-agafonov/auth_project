import requests
import sqlite3
from datetime import datetime


# креденшалы для БД
database = r'C:\Users\agafo\OneDrive\Desktop\udemy\django projects\logging_project\auth_cabinet\db.sqlite3'
table_from ='auth_app_linkstocheck'
table_to = 'auth_app_linkscheckresult'


# вот еще нужна валидация не пустая ли база
def check_links_in_db():

    print('начали проверку ссылок', datetime.now())

    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    result = cursor.execute('select * from {}'.format(table_from))
    fetch = result.fetchall()

    # проверяем не является ли запрос пустым
    if len(fetch) != 0:
        for_rows = []
        for i in fetch:
            index = i[0]
            original_link = i[1]
            upload_date = i[2]
            user_id = i[3]

            try:
                req = requests.get(original_link, allow_redirects=False)

                if req.status_code == 200:
                    original_link_status_code = str(req.status_code)
                    redirect_link = 'N/A'
                    redirect_link_status_code = 'N/A'
                    history = 'N/A'
                    history_check_date = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
                else:
                    original_link_status_code = str(req.status_code)

                    req = requests.get(original_link)
                    redirect_link = req.url
                    redirect_link_status_code = str(req.status_code)
                    history = str(req.history)
                    history_check_date = datetime.now().strftime('%Y/%m/%d %H:%M:%S')

            except:
                original_link_status_code = 'not valid link'
                redirect_link = 'N/A'
                redirect_link_status_code = 'N/A'
                history = 'N/A'
                history_check_date = datetime.now().strftime('%Y/%m/%d %H:%M:%S')

            new_row = (index, user_id, upload_date, original_link, original_link_status_code,
                       redirect_link, redirect_link_status_code,
                       history, history_check_date)


            for_rows.append(new_row)

        upload_conn = sqlite3.connect(database)
        upload_cursor = upload_conn.cursor()
        upload_cursor.executemany(
            'INSERT OR REPLACE INTO auth_app_linkscheckresult VALUES (?,?,?,?,?,?,?,?,?)', for_rows)
        upload_conn.commit()
        upload_conn.close()

        print('закончили проверку ссылок', datetime.now())


