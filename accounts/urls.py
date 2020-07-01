from django.conf.urls import *

from accounts import views as account_views
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    url(r'^signup/$', account_views.signup, {'template_name': 'accounts/signup.html' }, 'signup'),
    url(r'^profile/edit/$', account_views.edit_profile, {'template_name': 'accounts/edit_profile.html'}, 'edit_profile'),
    url(r'^profile/delete/$', account_views.delete_account, {}, 'delete_account'),
    url(r'^profile/confirm-delete/$', account_views.confirm_delete, {'template_name': 'accounts/confirm_delete.html'}, 'confirm_delete'),

    url(r'^$', auth_views.login, {'template_name': 'accounts/login.html'}, 'login'),
    url(r'^logout/$', auth_views.logout_then_login, name='logout'),

    url(r'^password/forgot/$', auth_views.password_reset, {'template_name': 'accounts/password_reset.html'}, name='password_reset'),
    url(r'^password/forgot/done/$', auth_views.password_reset_done, {'template_name': 'accounts/password_reset_done.html'}, name='password_reset_done'),

    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, {'template_name': 'accounts/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^password/reset/complete/$',
        auth_views.password_reset_complete, {'template_name': 'accounts/password_reset_complete.html'}, name='password_reset_complete'),
)
