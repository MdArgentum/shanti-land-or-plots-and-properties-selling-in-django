from django.shortcuts import render
from landapp.models import Land
# Create your views here.
def search(request):
    lands = Land.objects.order_by('name').filter(is_published=True)
    
    location_lands = Land.objects.values_list('location', flat=True).distinct()
    purpose_lands = Land.objects.values_list('purpose', flat=True).distinct()
    completion_lands = Land.objects.values_list('completion', flat=True).distinct()
    property_type_lands = Land.objects.values_list('property_type', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            lands = Land.objects.filter(short_description__icontains=keyword)
    
    if 'purpose_land' in request.GET:
        purpose_land = request.GET['purpose_land']
        if purpose_land:
            land = Land.objects.filter(purpose__iexact=purpose_land)

    if 'completion_land' in request.GET:
        completion_land = request.GET['completion_land']
        if completion_land:
            land = Land.objects.filter(completion__iexact=completion_land)

    if 'location_land' in request.GET:
        location_land = request.GET['location_land']
        if location_land:
            lands = Land.objects.filter(location__iexact=location_land)

    if 'property_type_land' in request.GET:
        property_type_land = request.GET['property_type_land']
        if property_type_land:
            land = Land.objects.filter(property_type__iexact=property_type_land)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            land = Land.objects.filter(price_total__gte=min_price, price_total__lte=max_price)

    context = {
        'land': lands,
        'completion_land': completion_lands,
        'location_land': location_lands,
        'purpose_land': purpose_lands,
        'property_type_land': property_type_lands,


    }
    return render(request, 'search/search.html', context)