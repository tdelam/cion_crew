from django.conf.urls import *

from skills import views

urlpatterns = patterns('',
    url(r'^profile/$', views.skills, {'template_name': 'skills/skills.html'}, 'skills'),
    url(r'^profile/view/(?P<user>\d+)$', views.view_user_skills, {'template_name': 'skills/skills.html'}, 'view_skills'),
    url(r'^profile/skills/edit/$', views.edit_skills, {'template_name': 'skills/edit_skills.html'}, 'edit_skills'),
    url(r'^profile/credits/edit/$', views.edit_credits, {'template_name': 'skills/edit_credits.html'}, 'edit_credits'),
    url(r'^add/$', views.add_skills, {'template_name': 'skills/add_skills.html'}, 'add_skills'),
    url(r'^directory/$', views.directory, {'template_name': 'skills/directory.html'}, 'directory'),
)