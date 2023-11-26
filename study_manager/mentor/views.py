from django.shortcuts import render
from django.views import View
from .models import Mentor
from student.models import student
from django.shortcuts import render, get_object_or_404,redirect
from .form import CreatTaskForm
from tasks.models import Tasks
from django.urls import reverse
# Create your views here.
class ShowStudent(View):
    def get(self,request,id):
        list_student=student.objects.filter(mentor_id=id)
        return render(request, 'mentor/all_student.html',{'list_student':list_student})
        

    def post(self,request):
        pass

class StudentDetail(View):
    def get(self,request,slug):
        student_obj=get_object_or_404(student,id=slug)
        # print("student detail1111111111111111111111111111111111111")
        ttasks_obj=Tasks.objects.filter(student_id=slug,situation="1")
        ftasks_obj=Tasks.objects.filter(student_id=slug,situation="0")
        return render(request, 'mentor/student_detail.html',{'student':student_obj,"ttasks":ttasks_obj,"ftasks":ftasks_obj})
    
class MentorProfile(View):
    def get(self,request,id):
        mentor_obj=Mentor.objects.get(member_id=id)

        return render(request, 'mentor/mentor_prof.html',{"mentor":mentor_obj})
    
class CreateTask(View):
    def get(self,request,id):
        # id student
        form=CreatTaskForm()
        mentor_id=student.objects.get(id=id).mentor_id
        content={
            "student":id,
            "mentor":mentor_id,
            "form":form}
        # print(form)
        return render(request, 'mentor/create_task.html',content)

    def post(self,request,id):
        print(request.POST)
        form = CreatTaskForm(request.POST)
        if form.is_valid():
            category=form.cleaned_data["category"]
            start_date=form.cleaned_data["start_date"]
            finish_date=form.cleaned_data["finish_date"]
            definitoin=form.cleaned_data["definitoin"]
            mentor_id=student.objects.get(id=id).mentor_id
            
            student_id=student.objects.get(id=id)
            task_model=Tasks(
                                category=category,
                                student_id=student_id,
                                mentor_id=mentor_id,
                                start_date=start_date,
                                finish_date=finish_date,
                                definitoin=definitoin,
                                situation="0"
                            )
            task_model.save()
            return render(request, 'mentor/student_detail.html',{'student':student_id})
        
class DeletTask(View):
    def get(self, request,id):
        # id task
        task_obj=Tasks.objects.get(id=id)
        student_id=task_obj.student_id.id
        task_obj.delete()
        return redirect(reverse("mentor:student_detail" , args=(student_id,)))
    

    
class DetailTask(View):
    def get(self, request,id):
        # id task
        task_obj=Tasks.objects.get(id=id)
        return render(request, 'mentor/detail_task.html',{'task':task_obj})

