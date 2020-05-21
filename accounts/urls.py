from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, re_path, reverse_lazy

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', LoginView.as_view(template_name='accounts/signin.html'), name='signin'),
    path('signout/', LogoutView.as_view(), name='signout'),
    path('need-signin/', views.need_signin, name='need_signin'),
    path('reset-password/', PasswordResetView.as_view(
        success_url=reverse_lazy('accounts:password_reset_done'),
        template_name='accounts/password_reset.html',
        email_template_name='accounts/password_reset_email.txt',
        subject_template_name='accounts/password_reset_subject.txt',
        html_email_template_name= 'accounts/password_reset_email.html'
    ), name='reset_password'),
    path('reset-password/done/',
         PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    re_path(r'password-reset-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            PasswordResetConfirmView.as_view(
                success_url=reverse_lazy('accounts:password_reset_complete'),
                template_name='accounts/password_reset_confirm.html'
            ),
            name='password_reset_confirm'),
    path('reset/complete/',
         PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
]
