from rest_framework import generics

from main_page.serializers import FoodListSerializer, DrinkListSerializer
from .models import Food, Drink


class FoodListView(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodListSerializer


class DrinkListView(generics.ListAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkListSerializer
