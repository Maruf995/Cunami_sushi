from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, User


# Create your models here.
class Food(models.Model):
    """Модель Еда"""
    name = models.CharField(verbose_name="Название еды", max_length=250)
    img = models.FileField(verbose_name="Фото еды", upload_to='food/')
    description = models.CharField(verbose_name="Описание еды", max_length=500)
    is_available = models.BooleanField(default=True, verbose_name="в Наличии")
    price = models.IntegerField(null=True)
    amount = models.IntegerField(null=True)
    new_price = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Еда"
        verbose_name_plural = "Еда"


class Drink(models.Model):
    """Модель Напитков"""
    name = models.CharField(verbose_name="Название Напитка", max_length=250)
    img = models.FileField(verbose_name="Фото Напитка", upload_to='drink/')
    description = models.CharField(verbose_name="Описание Напитка", max_length=500)
    is_available = models.BooleanField(default=True, verbose_name="в Наличии")
    price = models.IntegerField(null=True)
    amount = models.IntegerField(null=True)
    new_price = models.IntegerField(null=True)

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
