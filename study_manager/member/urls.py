from django.urls import path
from . import views

app_name="member"

urlpatterns=[

    path("login/",views.LoginView.as_view(),name="login"),
    
]