from django.http.response import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core import urlresolvers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms.models import modelformset_factory

from .models import CreditOptions, Skills
from .forms import SkillsForm, OptionFormset, BaseCreditFormSet


@login_required(login_url='/')
def skills(request, template_name):
    user = request.user
    try:
        skills = Skills.objects.get(user=user)
        credit_options = CreditOptions.objects.filter(user=user).order_by('crew_position', '-year')
    except Skills.DoesNotExist:
        return redirect(urlresolvers.reverse('add_skills'))
    return render(request, template_name, {
        'user': user,
        'credit_options': credit_options
    })

@login_required(login_url='/')
def view_user_skills(request, user, template_name):
    user = get_object_or_404(User, pk=user)
    skills = get_object_or_404(Skills, user=user)
    credit_options = CreditOptions.objects.filter(user=user).order_by('crew_position', '-year')
    return render(request, template_name, {
        'user': user,
        'skills': skills,
        'credit_options': credit_options
    })

@login_required(login_url='/')
def add_skills(request, template_name):
    user = request.user
    try:
        skills = Skills.objects.get(user=user)
    except Skills.DoesNotExist:
        skills_form = SkillsForm(label_suffix='')
        formset = OptionFormset()
        if request.method == 'POST':
            skills_form = SkillsForm(request.POST, request.FILES)
            if skills_form.is_valid():
                skill = skills_form.save(commit=False)
                skill.user = user
                skill = skills_form.save()
                formset = OptionFormset(request.POST)
                if formset.is_valid():
                    for form in formset.forms:
                        instance = form.save(commit=False)
                        instance.user = user
                        instance.save()
                    messages.success(request, "Successfully created your profile.")
                    return redirect(urlresolvers.reverse('skills'))
        return render(request, template_name, {
            'skills_form': skills_form,
            'formset': formset
        })
    else:
        messages.success(request, "You've already created a profile.")
        return redirect(urlresolvers.reverse('skills'))


@login_required(login_url='/')
def edit_skills(request, template_name):
    user = request.user
    skills_profile = get_object_or_404(Skills, user=user)
    if skills_profile.user != user:
        return HttpResponseForbidden("Sorry, something here doesn't make sense. Please try again.")
    if request.method == 'POST':
        form = SkillsForm(request.POST, request.FILES, instance=skills_profile, label_suffix='')
        if form.is_valid():
            form.save()
            messages.success(request, 'Your skills information has been updated.')
            url = urlresolvers.reverse('skills')
            return redirect(url)
    else:
        form = SkillsForm(instance=skills_profile)
    return render(request, template_name, {
        'skills_form': form,
    })


@login_required(login_url='/')
def edit_credits(request, template_name):
    user = request.user
    credits = CreditOptions.objects.filter(user=user).order_by('crew_position', '-year')
    
    EditFormSet = modelformset_factory(CreditOptions, formset=BaseCreditFormSet)

    if request.method == 'POST':
        formset = EditFormSet(request.POST)
        if formset.is_valid():
            for credit in credits:
                credit.delete()

            for form in formset.forms:
                instance = form.save(commit=False)
                instance.user = user
                instance.save()

            messages.success(request, "Successfully updated your credits.")
            return redirect(urlresolvers.reverse('skills'))
    else:
        formset = EditFormSet(queryset=credits)
    return render(request, template_name, {
        'formset': formset,
    })

def directory(request, template_name):
    skills = Skills.objects.all().order_by('user__last_name')
    return render(request, template_name, {
        'skills': skills,
    })