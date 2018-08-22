#_*_ conding.utf8_*_
from django.urls import path
from . import views

urlpatterns = [
    path('index/',    views.index,   name="index"),
    path('domain/',   views.domain,  name="domain"),
    path('user/',     views.user,    name="user"),
    path('help/',     views.help,    name="help"),
    path('login/',    views.login,   name="login"),
    path('admin/',    views.admin,   name="admin"),
    path('/',         views.index,   name="index"),
]
