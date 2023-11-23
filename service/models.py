from django.db import models
# Create your models here.
class Service(models.Model):
    """Model definition for Service."""

    # TODO: Define fields here
    service_id = models.CharField(max_length=2)
    icon = models.CharField( max_length=50)
    name = models.CharField(max_length=50)
    short_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        """Meta definition for Service."""

        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        """Unicode representation of Service."""
        return self.name

class Service_Video(models.Model):
    """Model definition for Service_Video."""
    description = models.TextField()
    video_url = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Service_Video."""

        verbose_name = 'Service_Video'
        verbose_name_plural = 'Service_Videos'

    def __str__(self):
        """Unicode representation of Service_Video."""
        return self.description

