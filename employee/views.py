from .models import *
from django.shortcuts import redirect, render,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):
    if request.user.is_active:
        employee = EmployeeInfo.objects.get(user = request.user)
        return render(request,'index.html',{'employee':employee})
    else:
        return redirect('/login/')


def edit(request):
    if request.user.is_active:
        employee = EmployeeInfo.objects.get(user = request.user)
        print(employee)
        if request.method == 'POST':
            fname = request.POST.get('fname')
            mname = request.POST.get('mname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            number = request.POST.get('number')
            age = request.POST.get('age')
            position = request.POST.get('position')
            address = request.POST.get('address')
            username = request.POST.get('username')
            image = request.FILES.get('image')

            if request.user.username != username:
                if User.objects.filter(username = username).exists():
                    messages.info(request,"the username is exists")
                    return render(request,'edit.html',{'employee':employee})
            
            user = User.objects.get(username = request.user)
            user.username = username
            user.save()

            employee.fname = fname
            employee.mname = mname
            employee.lname = lname
            employee.email = email
            employee.number = number
            employee.age = age
            employee.position = position
            employee.address = address
            if image is not None:
                employee.image = image
            employee.save()

            return redirect('/')

        contaxt = {
            'employee' : employee
        }

        return render(request,'edit.html',contaxt)
    else:
        return redirect('/login')



def register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        mname = request.POST.get('mname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        number = request.POST.get('number')
        age = request.POST.get('age')
        position = request.POST.get('position')
        address = request.POST.get('address')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_v = request.POST.get('passwordV')
        image = request.FILES.get('image')

        if User.objects.filter(username = username).exists():
            messages.info(request,"the username is exists")
            return render(request,'register.html')

        if password != password_v:
            messages.info(request,"Password dosnt match...")
            return render(request,'register.html')
        
        user = User(first_name = fname,last_name = lname ,email = email, username = username)
        user.set_password(password)
        user.save()

        employee = EmployeeInfo(user = user ,fname = fname,mname = mname , lname = lname,email = email,number = number,age = age , position = position , address = address,image = image)
        employee.save()

        return redirect('/login/')
        
        
    return render(request,'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password = password)
        if user is not None:
            if user.is_active:
                login(request,user)
                
                return redirect('/')
        else:
            messages.info(request,"Invalid Cardintial")
            return render(request,'login.html')
    
    return render(request,'login.html')


def logout_view(request):
    if request.user.is_active :
        logout(request)
        return redirect('/login/')
    else:
        return redirect('/login/')
    return redirect('/login/')
