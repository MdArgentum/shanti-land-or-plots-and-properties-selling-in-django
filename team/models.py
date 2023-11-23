from django.db import models

# Create your models here.
class Team(models.Model):
    """Model definition for Team."""
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    images = models.ImageField(upload_to='team/', height_field=None, width_field=None, max_length=None)
    facebook = models.URLField(max_length=200)
    twiter = models.URLField(max_length=200)
    google = models.URLField(max_length=200)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Team."""

        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        """Unicode representation of Team."""
        return self.name
