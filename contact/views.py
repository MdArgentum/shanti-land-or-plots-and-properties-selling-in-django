from django.shortcuts import render,get_object_or_404, redirect
from .models import Contact
from django.contrib import messages
def contact_page(request):
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
        contact = Contact.objects.create(name=name, email=email, subject=subject, phone=phone, message=message)
        messages.success(request, 'You are now logged in.') 
        contact.save()
        return redirect('contact_page')
    return render(request,'contact/contact_page.html')