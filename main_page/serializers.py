# from rest_framework import serializers
# from main_page.models import Food, Drink, Price, NewPrice


# class NewPriceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = NewPrice
#         fields = ['id', 'price']

# class FoodListSerializer(serializers.ModelSerializer):
#     price = serializers.SerializerMethodField(source='get_price')
#     class Meta:
#         model = Food
#         fields = '__all__'
#         # fields = "id name img description amount price".split()

#     def get_price(self, obj):
#         return obj.Price.name