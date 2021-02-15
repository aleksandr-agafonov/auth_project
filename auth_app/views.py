from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LogginForm, UserRegistrationForm
from django.http import HttpResponse
from .models import CallTouchModel, LinksToCheck, LinksCheckResult
import requests


# Create your views here.
def show_main_page(request):
    return render(request, 'main_page.html')


def registration(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration_success.html')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration.html', {'user_form': user_form})


def autharization(request):
    if request.method == 'POST':
        form = LogginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                # return render(request, 'main_page.html', {
                #     'user': user,
                #     'user_id': user.id
                # })
                return redirect('main_page')
            else:
                return HttpResponse('Неверный логи и / или пароль')
    else:
        form = LogginForm()
    return render(request, 'autharization.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('main_page')


@login_required
def go_to_cabinet(request):
    return render(request, 'cabinet.html')


@login_required
def create_calltouch(request):
    return render(request, 'create_calltouch.html')


@login_required
def validate_calltouch(request):
    try:
        node = request.POST['ct_node']
        cabinet_id = request.POST['ct_cabinet_id']
        token = request.POST['ct_token']
        start_date = request.POST['ct_start_date'],
        ct_days_back = request.POST['ct_days_back'],
        user_id = request.POST['user_id']

        req = requests.get(node)

        if req.status_code == 200:
            status_message = 'Креденшалы корректны!'

            ct_creds = CallTouchModel(
                ct_node=node,
                ct_token=token,
                ct_cabinet_id=int(cabinet_id),
                ct_user_id=int(user_id),
                ct_start_date=start_date[0],
                ct_days_back=int(ct_days_back[0]),
            )

            ct_creds.save()

            return render(request, 'new_calltouch_created.html', {
                'status_code': req.status_code,
                'status_message': status_message,
                'node': node,
                'cabinet_id': cabinet_id,
                'token': token,
                'start_date': start_date[0],
                'ct_days_back': ct_days_back[0],
            })

    except requests.ConnectionError:
        status_message = 'Ошибка в креденшалах!'
        return render(request, 'new_calltouch_created.html', {'status_message': status_message})


@login_required
def my_connections(request):
    connectors = CallTouchModel.objects.filter(ct_user_id=request.user.id)
    return render(request, 'my_connections.html', {'connectors': connectors})


@login_required
def links_input_form(request):
    return render(request, 'links_input_form.html')


@login_required
def send_links_to_check(request):
    links_content = request.GET['links_input']

    # проверяем не является ли поле пустым
    if len(links_content) == 0:
        error_message = 'Вы не ввели ссылки'
        return render(request, 'links_sent.html', {'error_message': error_message})

    else:
        links_content = links_content.split('\n')
        for link in links_content:
            link = link.replace('\r', '')
            print(link, type(link), request.user.id)
            links_to_check = LinksToCheck(
                links_original_link=link,
                links_user_id=request.user.id
            )
            links_to_check.save()

        return render(request, 'links_sent.html')


@login_required
def links_result(request):
    check_links_result = LinksCheckResult.objects.filter(user_id=request.user.id)
    return render(request, 'links_result.html', {'check_links_result': check_links_result})
