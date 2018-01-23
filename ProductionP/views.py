from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from PertaminaP import settings
from .forms import LoginForm

def Login(request):
    next = request.GET.get('next', '/home/')
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(next)
                else:
                    return HttpResponse("Inactive user.")
            else:
                return HttpResponseRedirect(settings.LOGIN_URL)
        else:
            return render(request, "index/login.html", {'redirect_to': next,'form': form,})
    else:
        form = LoginForm()

    return render(request, "index/login.html", {'redirect_to': next,'form': form,})

def Logout(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)

def Home(request):
    log_as = "You're login as %s" %(request.user)
    context = {
        "userlogin" : log_as
    }
    return render(request, "index/InputDisplay.html", context)

def Blog(request):
    return render(request, "index/blog.html", {})