from django.shortcuts import render
from django.views import View
from .models import Mentor
from student.models import student
from django.shortcuts import render, get_object_or_404
from .form import CreatTaskForm
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
        # print(student_obj.mentor)
        return render(request, 'mentor/student_detail.html',{'student':student_obj})
    
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
        return render(request, 'mentor/create_task.html',content)

    def post(self,request,id):
        pass 