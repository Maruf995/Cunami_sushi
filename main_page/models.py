from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, User


class FoodCategory(models.Model):
    """Категории к модели Еда"""
    name = models.CharField(max_length=255, verbose_name='Название категории', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Food(models.Model):
    """Модель Еда"""
    name = models.CharField(verbose_name="Название еды", max_length=250, unique=True)
    img = models.FileField(verbose_name="Фото еды", upload_to='food/')
    description = models.CharField(verbose_name="Описание еды", max_length=500)
    is_available = models.BooleanField(default=True, verbose_name="в Наличии")
    price = models.DecimalField(decimal_places=2, max_digits=7, null=True)
    amount = models.PositiveIntegerField(null=True)
    recommended = models.BooleanField(default=False, verbose_name='Рекомендованный')
    discount_price = models.PositiveIntegerField(verbose_name='Цена со скидкой')
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Еда"
        verbose_name_plural = "Еда"
        ordering = ['name']
        unique_together = (
            'name',
            'category'
        )


class Drink(models.Model):
    """Модель Напитков"""
    name = models.CharField(verbose_name="Название Напитка", max_length=250)
    img = models.FileField(verbose_name="Фото Напитка", upload_to='drink/')
    description = models.CharField(verbose_name="Описание Напитка", max_length=500)
    is_available = models.BooleanField(default=True, verbose_name="в Наличии")
    price = models.DecimalField(decimal_places=2, max_digits=7, null=True)
    amount = models.PositiveIntegerField(null=True)
    new_price = models.DecimalField(decimal_places=2, max_digits=7, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Напитки"
        verbose_name_plural = "Напитки"


class OrderStatus(models.Model):
    title = models.CharField(max_length=250, verbose_name='Статус заказа', unique=True)

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = "Статусы заказа"
        ordering = ['title']

    def clean(self):
        self.title = self.title.capitalize()

    def __str__(self):
        return self.title


class Order(models.Model):
    order_owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='order_owner', verbose_name='Заказчик')
    created_date = models.DateTimeField(verbose_name='Дата создания заказа', auto_now_add=True)
    total_price = models.FloatField(verbose_name='Итоговая стоимость заказа')
    order_status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, verbose_name='Статус заказа', default=1)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = "Заказы"
        ordering = ['created_date']

    def __str__(self):
        return f' Имя заказчика: {self.order_owner} | статус заказа: {self.order_status}'


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_products')
    link = models.CharField(max_length=250, verbose_name='Ссылка', null=True, blank=True)
    product_id = models.PositiveIntegerField(verbose_name='Артикул товара')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    price = models.PositiveIntegerField(verbose_name='Цена за единицу')
