from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Land(models.Model):
    """Model definition for Land."""
    reference_id = models.IntegerField()
    name = models.CharField(max_length=150, unique=True)
    name_slug = models.SlugField(unique=True)
    amount_land = models.CharField(max_length=50)
    price_per_katha = models.CharField(max_length=50, blank=True)
    price_total = models.CharField(max_length=50)
    area = models.CharField(max_length=250)
    location = models.CharField(max_length=50)
    previews_owner = models.CharField(max_length=50, blank=True)
    Current_owner = models.CharField(max_length=50, blank=True)
    google_map = models.URLField(max_length=2000)
    image = models.ImageField(upload_to='land/', max_length=None)
    image_1 = models.ImageField(upload_to='land/', max_length=None, blank=True)
    image_2 = models.ImageField(upload_to='land/', max_length=None, blank=True)
    image_3 = models.ImageField(upload_to='land/', max_length=None, blank=True)
    image_4 = models.ImageField(upload_to='land/', max_length=None, blank=True)
    image_5 = models.ImageField(upload_to='land/', max_length=None, blank=True, verbose_name='Slider Image')
    purpose = models.CharField(max_length=50)
    completion = models.CharField(max_length=50)
    property_category = models.CharField(max_length=50, blank=True)
    property_type = models.CharField(max_length=50, blank=True)
    short_description = RichTextField(max_length=2000)
    long_description = RichTextField(max_length=2500)
    is_featured = models.BooleanField(default=False)
    is_slider = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.name_slug:
            self.name_slug = slugify(self.name)
        super().save(*args, **kwargs)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Land."""

        verbose_name = 'Land'
        verbose_name_plural = 'Lands'

    def __str__(self):
        """Unicode representation of Land."""
        return self.name





