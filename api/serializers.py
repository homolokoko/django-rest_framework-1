from rest_framework import serializers
from client.models import Client
from drink.models import Drink
from payment.models import Payment

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
    
class DrinkSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Drink
        fields = '__all__'
        
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'