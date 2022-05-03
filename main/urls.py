from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('password_reset/', auth_views.PasswordResetView.as_view(template_name= 'navprayas/users/password_reset_form.html'), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name= 'navprayas/users/password_reset_done.html'), name='password_reset_done'),
    # path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name= 'navprayas/users/password_reset_confirm.html'), name='password_reset_confirm'),
    # path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name= 'navprayas/users/password_reset_complete.html'), name='password_reset_complete'),
    
    path('password_reset/', 
        auth_views.PasswordResetView.as_view(template_name='main/auth/password_reset_confirm.html'), 
        name='password_reset'),

    path('password_reset/done/', 
        auth_views.PasswordResetDoneView.as_view(template_name='main/auth/password_reset_done.html'), 
        name='password_reset_done'),
        
    path('password_reset/confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name= 'main/auth/password_reset_confirm.html'), 
        name='password_reset_confirm'),

    path('password_reset/complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name= 'main/auth/password_reset_complete.html'), 
        name='password_reset_complete'),

    path('login/', 
        auth_views.LoginView.as_view(template_name ='main/auth/login.html'), 
        name = 'login'),

    path('logout/', 
        auth_views.LogoutView.as_view(template_name= 'main/auth/logout.html'), 
        name='logout'),
    
    path("password_change/", 
        auth_views.PasswordChangeView.as_view(template_name ='main/auth/password_change_form.html'), name="password_change",),
    
    path("password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(template_name ='main/auth/password_change_done.html'),
        name="password_change_done",
    ),

    # path('accounts/', include('django.contrib.auth.urls')),
]
