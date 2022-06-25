from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, User
# Create your models here.

class Price(models.Model):
    """Доп Модель"""
    name = models.CharField(verbose_name='цена', max_length=250)
    price = models.IntegerField(null=True)

    def __str__(self):  
        return self.price



class NewPrice(models.Model):
    new_price = models.IntegerField(null=True)
    def __str__(self):
        return self.new_price

class Amount(models.Model):
    amount = models.IntegerField(null=True)
    def __str__(self):
        return self.amount

class Is_available(models.Model):
    is_available = models.BooleanField(default=True, verbose_name="в Наличии")
    def __str__(self):
        return self.is_available

class Food(models.Model):
    """Модель Еда"""
    name = models.CharField(verbose_name="Название еды", max_length=250)
    img = models.FileField(verbose_name="Фото еды", upload_to='food/')
    description = models.CharField(verbose_name="Описание еды", max_length=500)
    amount = models.IntegerField(Amount, null=True)
    is_available = models.BooleanField(default=True, verbose_name="в Наличии")
    price = models.IntegerField(null=True)
    new_price = models.IntegerField(NewPrice, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Еда"
        verbose_name_plural = "Еда"
    



class Drink(models.Model):
    """Модель Напитков"""
    name = models.CharField(verbose_name="Название напитка", max_length=250)
    img = models.FileField(verbose_name="Фото напитка", upload_to='drink/')
    description = models.CharField(verbose_name="Описание напитка", max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Напитки"
        verbose_name_plural = "Напитки"

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True)
    amount = models.IntegerField(null=False)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"