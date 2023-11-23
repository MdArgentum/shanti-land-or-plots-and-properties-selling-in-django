from django.db import models
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField

# Create your models here.
class About(models.Model):
    """Model definition for About."""
    name = models.CharField(max_length=50, verbose_name='Company Name')
    short_descripton = RichTextField(max_length=500)
    long_descripton = RichTextField(max_length=2500)
    
    image_1 = models.ImageField(upload_to='about/')
    image_2 = models.ImageField(upload_to='about/')
    image_3 = models.ImageField(upload_to='about/')

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for About."""

        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):
        """Unicode representation of About."""
        return self.name
