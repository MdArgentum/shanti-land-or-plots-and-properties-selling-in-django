from django.db import models

# Create your models here.
class Contact(models.Model):
    """Model definition for Contact."""
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    message = models.TextField(max_length=750)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Contact."""

        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        """Unicode representation of Contact."""
        return self.name

class Ltdinfo(models.Model):
    """Model definition for Ltdinfo."""
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254, blank=True)
    time = models.CharField(max_length=50)
    website = models.URLField(max_length=200)
    fax = models.CharField(max_length=50, blank=True)
    addres = models.CharField(max_length=250)
    facebook = models.URLField(max_length=200)
    twiter = models.URLField(max_length=200, blank=True)
    google = models.URLField(max_length=200, blank=True)
    youtube = models.URLField(max_length=200, blank=True)
    is_active = models.BooleanField(default=False)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Ltdinfo."""

        verbose_name = 'Ltdinfo'
        verbose_name_plural = 'Ltdinfos'

    def __str__(self):
        """Unicode representation of Ltdinfo."""
        return self.name
