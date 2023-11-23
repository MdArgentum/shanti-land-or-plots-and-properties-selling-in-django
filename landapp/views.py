from django.shortcuts import render,get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from team.models import Team
from .models import Land
# Create your views here.
def home(request):
    team = Team.objects.all()
    latest = Land.objects.filter(is_published=True)
    land = Land.objects.filter(is_slider=True, is_published=True)
    featured = Land.objects.filter(is_featured=True, is_published=True)

    #for search form
    location_land = Land.objects.values_list('location', flat=True).distinct()
    purpose_land = Land.objects.values_list('purpose', flat=True).distinct()
    completion_land = Land.objects.values_list('completion', flat=True).distinct()
    property_type_land = Land.objects.values_list('property_type', flat=True).distinct()
    context = {
        'team': team,
        'land': land,
        'latest': latest,
        'featured': featured,

        'completion_land': completion_land,
        'location_land': location_land,
        'purpose_land': purpose_land,
        'property_type_land': property_type_land,
    }
    return render(request, 'home.html', context)
def land(request):
    land = Land.objects.order_by('-created_at')
    paginator = Paginator(land, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    #for land page search form
    location_land = Land.objects.values_list('location', flat=True).distinct()
    purpose_land = Land.objects.values_list('purpose', flat=True).distinct()
    completion_land = Land.objects.values_list('completion', flat=True).distinct()
    property_type_land = Land.objects.values_list('property_type', flat=True).distinct()
    context = {
        'land': paged_cars,

        'completion_land': completion_land,
        'location_land': location_land,
        'purpose_land': purpose_land,
        'property_type_land': property_type_land,
    }
    return render(request, 'land/land.html', context)
def land_details(request, slug):
    land = get_object_or_404(Land, name_slug=slug)
    context = {
        'land': land,
    }
    return render(request, 'land/land_details.html', context)