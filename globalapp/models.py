from django.db import models

# Create your models here.
class GlobalAuth(models.Model):
    """Model definition for GlobalAuth."""
    title = models.CharField(max_length=250)
    featured_title = models.TextField()
    latest_title = models.TextField()
    team_title = models.TextField()
    service_title = models.TextField()
    contact_title = models.TextField()
    search_title = models.TextField()

    land_poster = models.ImageField(upload_to='poster_banner/')
    about_poster = models.ImageField(upload_to='poster_banner/')
    service_poster = models.ImageField(upload_to='poster_banner/')
    contact_poster = models.ImageField(upload_to='poster_banner/')
    search_poster = models.ImageField(upload_to='poster_banner/')
    login_poster = models.ImageField(upload_to='poster_banner/')
    register_poster= models.ImageField(upload_to='poster_banner/')
    dashboard_poster= models.ImageField(upload_to='poster_banner/')

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for GlobalAuth."""

        verbose_name = 'GlobalAuth'
        verbose_name_plural = 'GlobalAuths'

    def __str__(self):
        """Unicode representation of GlobalAuth."""
        return self.title
