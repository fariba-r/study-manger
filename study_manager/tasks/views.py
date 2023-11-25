from django.shortcuts import render,redirect
from django.urls import reverse
from django.views import View
from .models import Tasks

class StudentFTask(View):
    def get(self, request,slug):
        tasks_obj=Tasks.objects.filter(student_id=slug,situation="0")
        # print(tasks_obj)
        content={'tasks':tasks_obj}
        return render(request,"tasks/show_ftasks.html",content)

class StudentTTask(View):
    def get(self, request,slug):
        tasks_obj=Tasks.objects.filter(student_id=slug , situation="1")
        content={'tasks':tasks_obj}
        return render(request,"tasks/show_ttasks.html",content)

class DetailTask(View):
    def get(self, request,id):
        task_obj=Tasks.objects.get(id=id)
        print(task_obj.situation,task_obj.categoy)
        if task_obj.situation:
            return render(request,"tasks/detail_ttask.html",{"task":task_obj})
        else:
            return render(request,"tasks/detail_ftask.html",{"task":task_obj})
        
class Done_task(View):
    def get(self, request,id):
        ttask_obj=Tasks.objects.get(id=id)
        
        # ttask_obj.situation="1"
        # ttask_obj.save()
        Tasks.objects.filter(id=id).update(situation="1")
        student_id=ttask_obj.student_id.id
       
        return redirect(reverse("tasks:show_ftasks" , args=(student_id,)))
        
        

