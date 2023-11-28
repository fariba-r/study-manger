from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from .models import student
from tasks.models import Tasks
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch


class StuProfile(View,LoginRequiredMixin):
    
    def get(self, request,id):
        student_obj=student.objects.get(member_id=id)
        count_ttask=Tasks.objects.filter(student_id=student_obj.id, situation='1').count()
        count_ftask=Tasks.objects.filter(student_id=student_obj.id, situation='0').count()
        
        return render(request,"student/stu_prof.html",{"student":student_obj,"count_ttask":count_ttask,"count_ftask":count_ftask})
    
# class ShowAllTTasks(View):
#     def get(self, request,id):
#         tasks_obj=Tasks.objects.select_related(student_id=id,situation=True)
#         return render(request,"show_tasks.html",{"task":tasks_obj})

# class ShowAllFTasks(View):
#     def get(self, request,id):
#         tasks_obj=Tasks.objects.select_related(student_id=id,situation=False)
#         return render(request,"show_tasks.html",{"task":tasks_obj})
    
