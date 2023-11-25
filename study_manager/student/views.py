from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from .models import student
from tasks.models import Tasks

class StuProfile(View):
    def get(self, request,id):
        student_obj=student.objects.get(member_id=id)
        
        return render(request,"student/stu_prof.html",{"student":student_obj})
    
# class ShowAllTTasks(View):
#     def get(self, request,id):
#         tasks_obj=Tasks.objects.select_related(student_id=id,situation=True)
#         return render(request,"show_tasks.html",{"task":tasks_obj})

# class ShowAllFTasks(View):
#     def get(self, request,id):
#         tasks_obj=Tasks.objects.select_related(student_id=id,situation=False)
#         return render(request,"show_tasks.html",{"task":tasks_obj})
    
