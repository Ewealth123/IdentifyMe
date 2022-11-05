from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from account.models import agent
from account.models import Profile

from django.contrib import messages
from django.contrib.auth.models import User, auth
from .helpers import send_password
import uuid
# Create your views here.
def register(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        password = request.POST['password']
        con_password = request.POST['con_password']
        if   password==con_password:
            if agent.objects.filter(email=email).exists():
                messages.info(request, 'Email already Exist')
                return redirect('register')
            else:
                reg = agent(full_name=full_name,email=email,password=password,wallet_bal = '0')
                reg.save()
                user = User.objects.create_user(username=email, password=password, first_name = full_name)
                user.save();
                messages.info(request, 'Registration successfull, please login!')
                return redirect('login')
            
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
    else:
        return render(request, 'login.html')

def login(request):
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(username=email, password=password)
        
        if user is not None:
            auth.login(request, user)
            
            return redirect("dashboard")
            
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:    
        return render(request, 'login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('login')

def password_reset(request):
    
    try:
        if request.method=="POST":
            email = request.POST.get('email')
            
            if not  User.objects.filter(username=email).first():
                messages.info(request, 'This account is not associated with this email address.')
                return redirect('password_reset')
            
            user_obj = User.objects.get(username = email)
            print(user_obj)
            token= str(uuid.uuid4())
            profile_obj = agent.objects.get(email = user_obj)
            profile_obj.forget_password_token = token
            profile_obj.save()
            send_password(user_obj.username, token)
            messages.info(request, 'Visit your mail for your Password Reset link. Check your spam folder if you cannot find the mail. ')
            return redirect('password_reset')
    
    except Exception as e:
        print(e)
    return render(request, "password_reset.html")

def change_password(request, token):
    context = {}
    try:
        profile_obj = agent.objects.filter(forget_password_token = token).first()
        context = { 'user_id' : profile_obj.email}
        if  request.method == 'POST':
            new_password =  request.POST.get('password')
            con_password = request.POST.get('con_password')
            user_id = request.POST.get('user_id')
            
            if new_password != con_password:
                messages.info(request, 'Password mismatch. ')
                return redirect('change-password')
            
            user_obj = User.objects.get(username=user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            agent.objects.filter(email = user.username).update(password = new_password)
            messages.info(request, 'Password changed successfully. ')
            return redirect('login')
        
    
    except Exception as e:
        print(e)
    return render(request, "password_reset_form.html", context)