from django.shortcuts import render,redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views import View
# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import HttpResponse
from .form import LoginForm
from student.models import student
from mentor.models import Mentor
from .models import Members
from django.contrib.auth.hashers import make_password
import datetime
class LoginView(View):
    def post(self, request):
        
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            try:
                student_obj=student.objects.get(member_id=user.id)
                    
                return redirect(reverse('student:stu_profile', args=(user.id,)))
            
            except:
                mentor_obj=Mentor.objects.get(member_id=user.id)
                
                return redirect(reverse('mentor:mentor_profile', args=(user.id,)))
            
        else:
            
            return redirect(reverse("member:login"))
            

    def get(self, request):
        form={"form":LoginForm()}
        
        return render(request,"member/login.html",form)
    
class SignUpView(View):
    def get(self, request):
        
        return render(request,"member/signup.html")

    def post(self, request):
        print(request.POST)
        member_obj=Members(

                                        mobile_number =request.POST.get('mobile_number'),
                                        
                                        gender =request.POST.get('gender'),
                                        first_name=request.POST.get('fname'),
                                        last_name=request.POST.get('lname'),
                                        birthday=request.POST.get('birthday'),
                                        address=request.POST.get('adress'),
                                        password=make_password(request.POST.get('password')),
                                        username=request.POST.get('username'),
                                        is_superuser=True,
                                        is_staff=True,
                                        is_active=True
                                        )
        member_obj.save()
        # print(request.POST.get('role'))

        if request.POST.get('role')=='student':
            
            return redirect(reverse('member:student_signup', args=(member_obj.id,)))
        else:
            
            return redirect(reverse('member:mentor_signup', args=(member_obj.id,)))
        

class StudentSignup(View,SuccessMessageMixin):
    def get(self, request,id):
        # id member
        mentor=Mentor.objects.all()
        return render(request,"member/student_signup.html",{"mentors":mentor})

    def post(self, request,id):
        member_obj=Members.objects.get(id=id)
        mentor_obj=Mentor.objects.get(id=request.POST.get('mentor_id'))
       
        student_obj=student(
                                        member_id=member_obj,
                                        grade=request.POST.get('grade'),
                                        mentor_id=mentor_obj
                                        
                                        )
        
        student_obj.save()
        success_message = 'List successfully saved!!!!'
        
        print(request)
        return redirect(reverse("member:login"))

class MentorSignup(View):
    def get(self, request,id):
        # id member
        
        return render(request,"member/mentor_signup.html")
    
    def post(self, request,id):
        
        
        member_obj=Members.objects.get(id=id)
        
        mentor_obj=Mentor(
                                        member_id=member_obj,
                                        date_employment=datetime.datetime.now(),
                                        salary=request.POST.get('salary')
                                        )
        
        mentor_obj.save()
        return redirect(reverse("member:login"))


        