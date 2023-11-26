from django.urls import path
from . import views
app_name="mentor"
urlpatterns=[
    path('detail_task/<int:id>/',views.DetailTask.as_view(),name="detail_task"),
    path('all_student/<int:id>/',views.ShowStudent.as_view(),name="all_student"),
    path('mentor_profile/<int:id>/',views.MentorProfile.as_view(),name="mentor_profile"),
   
    path('create_task/<int:id>/',views.CreateTask.as_view(),name="create_task"),
    path("delet_task/<int:id>/",views.DeletTask.as_view(),name="delet_task"),
    path('<slug:slug>/',views.StudentDetail.as_view(),name="student_detail"),
    
]