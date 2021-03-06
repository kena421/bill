from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import navbar, index, signup, profile, student_home, teacher_home, portal_selection, subject_assignments, view_assignment

urlpatterns = [
    
    path('password_reset/', 
        auth_views.PasswordResetView.as_view(template_name='main/auth/password_reset_email.html'), 
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




    ########################################################################################

    path(
        'sample/', 
        navbar,
        name='navbar'
    ),

    path(
        '', 
        index,
        name='index'
    ),

    path(
        '', 
        index,
        name='index'
    ),
    path(
        'signup/', 
        signup,
        name='signup'
    ),

    path(
        'profile/', 
        profile,
        name='profile'
    ),

    path(
        'portal_selection/', 
        portal_selection,
        name='portal_selection'
    ),

    path(
        'student_home/', 
        student_home,
        name='student_home'
    ),

    path(
        'teacher_home/', 
        teacher_home,
        name='teacher_home'
    ),

    path(
        'subject_assignments/<int:id>', 
        subject_assignments,
        name='subject_assignments'
    ),

    path(
        'assignment/<int:id>', 
        view_assignment,
        name='view_assignment'
    ),

]
