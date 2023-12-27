from rest_framework.response import Response
from rest_framework.decorators import api_view
from client.models import Client
from .serializers import ClientSerializer, DrinkSerializer, PaymentSerializer
from drink.models import Drink
from rest_framework import status
from payment.models import Payment

from django.http import JsonResponse

@api_view(['GET'])
def getUser(request):
    user = Client.objects.all()
    serializer = ClientSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postUser(request):
    serializer = ClientSerializer(data=request.data)
    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getDrinks(request):
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def detailDrink(request, id):
    
    try :
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializers = DrinkSerializer(drink)
        return Response(serializers.data)
        
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE': 
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def getPayment(request):
    payments = Payment.objects.all()
    serializers = PaymentSerializer(payments, many=True)
    return Response(serializers.data)