from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm, UserAuthenticationForm


@login_required(login_url='account:sign_up')
def profile(request):
    return render(request, template_name='account/profile.html')


def sign_up(request):
    context = {}
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        context.update({'form': form})
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('account:profile')
    else:
        form = UserRegistrationForm()
        context.update({'form': form})
    return render(request, template_name='account/sign_up.html', context=context)


def sign_in(request):
    context = {}
    if request.method == 'POST':
        form = UserAuthenticationForm(request.POST)
        context.update({'form': form})
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect('account:profile')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = UserAuthenticationForm()
        context.update({'form': form})
    return render(request, template_name='account/sign_in.html', context=context)


def logout():
    pass
