from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from .views import *
from .forms import RestPasswordForm

urlpatterns = [
    path('', home, name='home_page'),
    path('register/', register_new_users, name='register_page'),
    path('login/', login_user, name='login_page'),
    path('logout/', logout_user, name='logout_user'),
    path('change_password/', change_password, name='change_password'),
    path('edit_profile/', edit_profile, name='user_profile'),

    # path('password_reset',
    #      auth_views.PasswordResetView.as_view(template_name='users/email_password_reset.html',),
    #      name='reset_email'),
    #
    # path('password_reset/done',
    #      auth_views.PasswordResetDoneView.as_view(template_name='users/email_sent.html',),
    #      name='email_sent'),
    #
    # path('password_reset_done',
    #      auth_views.PasswordResetConfirmView.as_view(),
    #      name='password_reset_confirm'),

    re_path(r'^password_reset/$', auth_views.PasswordResetView.as_view(template_name='users/email_password_reset.html',),
            name='password_reset'),

    re_path(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(
        template_name='users/email_sent.html'), name='password_reset_done'),

    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset.html', form_class=RestPasswordForm),
            name='password_reset_confirm'),

    re_path(r'^reset/done/$',
            auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_done.html',),
            name='password_reset_complete'),


    # path('reset_email', email_password_reset, name='reset_email'),
    # path('password_reset', password_reset, name='reset_password'),
]
