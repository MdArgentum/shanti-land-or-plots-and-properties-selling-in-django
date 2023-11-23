from django.db import models

# Create your models here.

class Inquiry(models.Model):
    """Model definition for inquiry."""
    status_choices = (
        ('Under Review', 'Under Review'),
        ('Unread Yet', 'Unread Yet'),
        ('Read it', 'Read it'),
        ('Contact to you as soon as possible', 'Contact to you as soon as possible'),
    )

    user_id = models.IntegerField()
    first_name = models.CharField(max_length=50)                      
    last_name = models.CharField(max_length=50)                      
    question = models.CharField(max_length=50)                      
    name = models.CharField(max_length=50)                      
    city = models.CharField(max_length=50)                      
    division = models.CharField(max_length=50)    
    email = models.EmailField(max_length=254)                  
    phone = models.CharField(max_length=50)    
    message = models.TextField()  
    status = models.CharField(choices=status_choices, default='Unread Yet', max_length=50)

    created_at = models.DateField(auto_now_add=True)                
    updated_at = models.DateField(auto_now_add=True)                

    # TODO: Define fields here

    class Meta:
        """Meta definition for inquiry."""

        verbose_name = 'inquiry'
        verbose_name_plural = 'inquiries'

    def __str__(self):
        """Unicode representation of inquiry."""
        return self.name
