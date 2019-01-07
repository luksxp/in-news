from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    slug = models.SlugField(default=0)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    def __str__(self): 
        return self.name
        
class Link(models.Model):
    """Model representing a specific link."""
    title = models.CharField(max_length=128)
    url = models.URLField(default=0) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=0)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title
        
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('link_detail', args=[str(self.id)])
        

        
    

        
    



        
   
