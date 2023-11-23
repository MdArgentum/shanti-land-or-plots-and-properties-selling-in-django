from django.shortcuts import render
from .models import Service, Service_Video
# Create your views here.
def service_page(request):
    service = Service.objects.all()
    item = Service_Video.objects.first()
    context = {
        'service':service,
        'item':item,
    }
    return render(request, 'service/service_page.html', context)