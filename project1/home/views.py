from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader
from django.urls import reverse 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from .models import Student
from .forms import EmpForm
from .filters import StuCredentials

def welcome(request):
    return render(request, "home/welcome.html")

def signup(request):
    if request.method =="POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        myuser= User.objects.create_user(username,email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        
        myuser.save()
        messages.success(request, "Your Account has been successfully created.")
        
        return HttpResponseRedirect('signin')
    return render(request, "home/signup.html")


def signin(request):
    if request.method =='POST':
        username = request.POST['username']
        pass1= request.POST['pass1']
        email= request.POST['email']
        
        user= authenticate(username=username, password=pass1, email=email)
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "home/welcome.html", {'fname': fname})
        else:
            messages.error(request, 'Bad Credentials')
            return HttpResponseRedirect(reverse('home:welcome'))
    return render(request, "home/signin.html")

def signout(request):
    logout(request)
    messages.success(request,'Logged Out Succesfully!')
    return redirect('home:welcome')

def index(request):  
    if request.method=='POST':
        stu = EmpForm(request.POST)
        
        if stu.is_valid():
            stu1= stu.cleaned_data['studentID']
            stu2= stu.cleaned_data['name']
            stu3= stu.cleaned_data['email']
            stu4= stu.cleaned_data['password']
        #   older version update method   
        #    reg = Student(stuid= stu1,stuname=stu2, stuemail=stu3, stupass=stu4)
        #    reg.save()
            stu.save()
    else:
        stu= EmpForm()
            
    return render(request,"home/index.html",{'form':stu})  

def studentinfo(request):
    stud=Student.objects.all()
    stu_count=stud.count()
    myFilter=StuCredentials(request.POST, queryset=stud)
    stud=myFilter.qs
            
    context={
        'stu':stud,
        'stu_count':stu_count,
        'myFilter':myFilter
        }
    
def update(request, _id_=None):
    stud = Student.objects.get(id=_id_)
    template=loader.get_template('home/update.html')
    context = {
    'stu': stud,
     }
    return HttpResponse(template.render(context, request))

def delrec(request, _id=None):
    deletestu=Student.objects.get(id=_id)
    deletestu.delete()
    stud=Student.objects.all()
    return render(request, 'home/studetails.html',{'stu':stud} )