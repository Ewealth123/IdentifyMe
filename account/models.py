from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class agent(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    wallet_bal = models.CharField(max_length=1000)
    password = models.CharField(max_length=100)
    forget_password_token = models.CharField(max_length=100)
    
    
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    forget_password_token  = models.CharField(max_length=100)
    date_created =models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.user.username