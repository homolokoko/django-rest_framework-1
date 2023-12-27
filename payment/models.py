from django.db import models
from client.models import Client
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.
class Payment(models.Model):
    purpose = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="user_id")
    
    def __str__(self):
        return self.purpose+' : '+self.user.client_name
