from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from .models import Food
from rest_framework.response import Response
from main_page.serializers import FoodListSerializer

# Create your views here.
@api_view(['GET'])
def food_view(request):
    food = Food.objects.all()

    data = FoodListSerializer(food, many=True).data

    return Response(data=data)