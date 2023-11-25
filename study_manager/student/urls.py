from django.urls import path
from . import views



app_name='student'

urlpatterns=[
path("stu_profile/<int:id>/",views.StuProfile.as_view(),name="stu_profile"),
# path("all_false_tasks/<int:id>/",views.ShowAllFTasks.as_view(),name="aftasks"),
# path("all_true_tasks/<int:id>/",views.ShowAllTTasks.as_view(),name="attasks"),
]