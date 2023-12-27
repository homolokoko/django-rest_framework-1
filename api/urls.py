from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.getUser),
    path('user/add', views.postUser),
    path('drinks/', views.getDrinks),
    path('drink/<int:id>', views.detailDrink),
    path('payment', views.getPayment)
]
