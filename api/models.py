from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Products')
    name = models.CharField(max_length=225)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __string__(self):
        return self.name