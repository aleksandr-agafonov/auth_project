"""
WSGI config for auth_cabinet project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

# import os
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auth_cabinet.settings')
#
# application = get_wsgi_application()

# import os
# import sys
#
# # add your project directory to the sys.path
# project_home = '/home/afgafonov/auth_app/test_auth_app'
# if project_home not in sys.path:
#     sys.path.insert(0, project_home)
#
# # set environment variable to tell django where your settings.py is
# os.environ['DJANGO_SETTINGS_MODULE'] = 'test_auth_app.settings'
#
#
# # serve django via WSGI
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()


import os
import sys

# assuming your Django settings file is at '/home/myusername/mysite/mysite/settings.py'
path = 'auth_cabinet\auth_cabinet'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

## Uncomment the lines below depending on your Django version
###### then, for Django >=1.5:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
###### or, for older Django <=1.4
#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()