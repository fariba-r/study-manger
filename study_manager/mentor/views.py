from django.shortcuts import render
from django.views import View
from student.models import student
from django.shortcuts import render, get_object_or_404
# Create your views here.
class ShowStudent(View):
    def get(self,request):
        list_student=student.objects.all()
        return render(request, 'all_student.html',{'list_student':list_student})
        

    def post(self,request):
        pass

class StudentDetail(View):
    def get(self,request,slug):
        student_obj=get_object_or_404(student,id=slug)
        # print(student_obj.mentor)
        return render(request, 'student_detail.html',{'student':student_obj})