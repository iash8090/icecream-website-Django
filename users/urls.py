from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.loginCustomer, name="loginCustomer"),
    path('logout/',views.logoutCustomer,name="logoutCustomer"),

# There are predefined class based View in django to reset password, which we have imported above as auth_views 
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset-password"),
    path('reset_password_sent/', auth_views.PasswordChangeDoneView.as_view(), name="reset-password-sent"),

# name of this path should be exactly this "password_reset_confirm"
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="reset-password-complete"),
]


""" 
1. Submit email form -                      accounts/password_reset/ [name='password_reset']
2. Email sent success message -             accounts/password_reset/done/ [name='password_reset_done']
3. Link to password reset form in email -   accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
4. Password successfully changed message -  accounts/reset/done/ [name='password_reset_complete']
 """
