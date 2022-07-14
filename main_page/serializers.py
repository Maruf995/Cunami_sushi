from rest_framework import serializers
from main_page.models import Food, Drink


class FoodListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class DrinkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = '__all__'

# class FoodDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Food
#         fields = ['id', 'name', 'img', 'description']
