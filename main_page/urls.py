from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/food/', FoodListView.as_view()),
    path('api/v1/drink/', DrinkListView.as_view())
]
