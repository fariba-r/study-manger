from django.urls import path
from . import views
app_name="tasks"
urlpatterns =[

    path("ftask/<slug:slug>/",views.StudentFTask.as_view(),name="show_ftasks"),
    path("ttask/<slug:slug>/",views.StudentTTask.as_view(),name="show_ttasks"),
    path("detail_task/<int:id>/",views.DetailTask.as_view(),name="show_detail"),
    path("done_task/<int:id>/",views.Done_task.as_view(),name="done_task"),
    

]