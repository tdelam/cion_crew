from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core import urlresolvers
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import UserProfile
from .forms import SignupForm, EditProfileForm


def signup(request, template_name):
    if request.method == 'POST':
        post_data = request.POST.copy()
        form = SignupForm(post_data)
        if form.is_valid():
            form.save()
            messages.success(request, "You've successfully signed up.")
            return redirect(urlresolvers.reverse('login'))
    else:
        form = SignupForm(label_suffix='')
    return render(request, template_name, {
        'form': form
    })

@login_required(login_url='/')
def edit_profile(request, template_name):
    user = request.user
    profile = get_object_or_404(UserProfile, user=user)
    if profile.user != user:
        return HttpResponseForbidden("Sorry, something here doesn't make sense. Please try again.")
    if request.method == 'POST':
        form = EditProfileForm(data=request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your contact information has been updated.')
            url = urlresolvers.reverse('skills')
            return redirect(url)
    else:
        form = EditProfileForm(instance=profile)
    return render(request, template_name, {
        'form': form,
    })


@login_required(login_url='/')
def delete_account(request):
    user = request.user
    profile = get_object_or_404(UserProfile, user=user)
    if profile.user != user:
        return HttpResponseForbidden("Sorry, something here doesn't make sense. Please try again.")
    url = urlresolvers.reverse('confirm_delete')
    return redirect(url)


@login_required(login_url='/')
def confirm_delete(request, template_name):
    user = request.user
    profile = get_object_or_404(UserProfile, user=user)
    if profile.user != user:
        return HttpResponseForbidden("Sorry, something here doesn't make sense. Please try again.")
    if request.method == 'POST':
        account = get_object_or_404(User, username=user.email)
        account.is_active = False
        account.save()
        logout(request)
        url = urlresolvers.reverse('signup')
        return redirect(url)
    return render(request, template_name, {})