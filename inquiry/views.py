from django.shortcuts import render, redirect
from .models import Inquiry
from django.contrib import messages
# Create your views here.

def inquiry(request):
    if request.method =='POST':
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        question = request.POST['customer_need']
        name = request.POST['land_title']
        city = request.POST['city']
        division = request.POST['division']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        inquiry = Inquiry.objects.create(user_id=user_id,first_name=first_name, last_name=last_name,question=question, name=name, city=city,division=division,email=email,phone=phone,message=message)

        inquiry.save()
        messages.success(request,'Your Message has been Sent!')
        return redirect('dashboard')