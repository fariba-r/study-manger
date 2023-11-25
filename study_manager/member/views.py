from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import HttpResponse
from .form import LoginForm
from student.models import student
from mentor.models import Mentor

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