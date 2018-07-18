from django.shortcuts import render

def index(request):
    content = {}
    content['aaa'] = 'index    index'
    return render(request, 'index/index.html', content)

def domain(request):
    content={}
    content['aaa'] = 'index    index'
    return render(request, 'domain/domain.html', content)

def user(request):
    content = {}
    content['aaa'] = 'index    index'
    return render(request, 'user/user.html', content)

def help(request):
    content = {}
    content['aaa'] = 'index    index'
    return render(request, 'help/help.html', content)

def login(request):
    content = {}
    content['aaa'] = 'index    index'
    return render(request, 'login/login.html', content)

def admin(request):
    content = {}
    content['aaa'] = 'admin   admin'
    return render(request, 'admin/admin.html', content)
