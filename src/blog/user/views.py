from django.shortcuts import render,reverse

from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from user.forms import UserForm


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username= username, password=password)
            if user is not None:
                auth_login(request,user)
                return HttpResponseRedirect('/')
        context = {
            'title':'login',
            'error':True,
            'message':'Invalid username or password'
        }
        return render(request, 'users/login.html',context=context)
    else:
        context = {
            'title':'Login'
        }
        return render(request,'users/login.html',context=context)



def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse("web:index"))


def signup(request):
    form = UserForm()
    context = {
        "title":"signup",
        "form":form
    }
    return render(request, 'users/signup.html', context=context)