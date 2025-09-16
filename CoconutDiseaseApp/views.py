from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
import os
from django.core.mail import send_mail

from .models import *
from .forms import *
from .predict import process

# Create your views here.
def index(request):
    return render(request,'auth/login.html')

def logout(request):
    request.session.clear()
    return redirect('index')

def login_view(request):
    return render(request,'auth/login.html')

def register_view(request):
    return render(request,'auth/register.html')

def createAccount(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            response = {
                'status': True,
                'message': 'User Created Successfully'
            }
            return JsonResponse(response)
        else:
            # Form is not valid, extract error messages
            errors = form.errors
            print(errors)
            error_message = str(errors['contact'][0]) if 'contact' in errors else str(errors['email'][0]) if 'email' in errors  else 'Invalid form data'

            response = {
                'status': False,
                'message': error_message
            }
            return JsonResponse(response)
        
    return JsonResponse({ 'status':False, 'message':'Invalid Request Method!' })

def loginAccount(request):
    if request.method=='POST':
        response={
            'status':False,
            'message':'Invalid Request Method!'
        }
           
        email = request.POST['email']
        password = request.POST['password']
        
        user = User.objects.filter(email=email, password=password,is_active=1).first()

        if user is None:
            response={
                'status':False,
                'message':'Invalid User'
            }
        else:
            request.session['userId']=user.id
            
            response={
                'status':True,
                'message':'Successfully logged in'
            }
           
    return JsonResponse(response)


def home_view(request):
    return render(request,'home/home.html')

def upload(request):
    return render(request,'home/upload.html')

def detect_disease(request):
    if request.method == 'POST':

        image = request.FILES['image']

        image_name = 'input.jpg'
        image_path = os.path.join(settings.MEDIA_ROOT, image_name)

        with open(image_path, 'wb+') as destination:
            for chunk in image.chunks():
                destination.write(chunk)

        response = process(image_path)

        userId=request.session['userId']

        user = User.objects.get(id=userId)
        if user:
            # Send email to the user with the disease details
            # send_disease_email(user.email, response)
            print("Email sent to user:", user.email)

        return JsonResponse({ 'status':True, 'message':"Success",'data':response })
    else:
        return JsonResponse({ 'status':False, 'message':'Invalid Request Method!' })
    

def send_disease_email(to_email, disease):
    remedies_formatted = "\n".join([f"• {r}" for r in disease['remedies']])

    subject = f"Disease Detected: {disease['title']}"
    message = f"""
Hello,

The disease detection process has completed. Here are the details:

🦠 Disease: {disease['title']}

📋 Description:
{disease['description']}

💊 Remedies:
{remedies_formatted}

Stay safe and take appropriate action.

Regards,
Your Coconut Health System
    """

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [to_email],
        fail_silently=False,
    )