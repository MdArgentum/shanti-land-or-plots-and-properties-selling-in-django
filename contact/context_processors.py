from .models import Ltdinfo
from globalapp.models import GlobalAuth  # Import your Ltdinfo model

def ltdinfo_info(request):
    # Fetch data from the Ltdinfo model or perform any required logic
    ltdinfo_data = Ltdinfo.objects.first()  # Retrieve the first Ltdinfo object (you can customize this query as needed)
    return {'ltdinfo_info': ltdinfo_data}  # Return the contact data to be available in templates

def globalapp_info(request):
    # Fetch data from the globalapp model or perform any required logic
    globalapp_data = GlobalAuth.objects.first()  # Retrieve the first globalapp object (you can customize this query as needed)
    return {'globalapp_info': globalapp_data}  # Return the contact data to be available in templates
