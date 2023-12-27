from django.db import models
from client.models import Client

# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=100, null=False)
    customer_age = models.IntegerField(null=False)
    customer_gender = models.CharField(max_length=6, null=False)
    customer_phone = models.CharField(max_length=10, null=False)
    customer_email = models.EmailField(null=True)
    customer_add = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.client_name+' => '+self.customer_name
