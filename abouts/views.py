from django.shortcuts import render
from team.models import Team
from .models import About
# Create your views here.
def about_page(request):
    team = Team.objects.all()
    about = About.objects.first()
    context = {
        'team': team,
        'about': about,
    }
    return render(request,'abouts/about_page.html', context)