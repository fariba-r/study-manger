from django.urls import path
from . import views
app_name="mentor"
urlpatterns=[

    path('all_student/',views.ShowStudent.as_view(),name=""),
    path('<slug:slug>/',views.StudentDetail.as_view(),name="student_detail"),

]