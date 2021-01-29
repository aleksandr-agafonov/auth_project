from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LogginForm, UserRegistrationForm, CallTouchForm
from django.http import HttpResponse


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
                #return render(request, 'main_page.html', {'user': user})
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
    form = CallTouchForm()
    return render(request, 'create_calltouch.html', {'form': form})