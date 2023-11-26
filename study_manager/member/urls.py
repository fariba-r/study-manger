from django.urls import path
from . import views

app_name="member"

urlpatterns=[

    path("login/",views.LoginView.as_view(),name="login"),
    path("signup/",views.SignUpView.as_view(),name="signup"),
    path("student_signup/<int:id>",views.StudentSignup.as_view(),name="student_signup"),
    path("mentor_signup/<int:id>/",views.MentorSignup.as_view(),name="mentor_signup"),
    
]