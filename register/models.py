from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, User
from django.contrib.auth.validators import UnicodeUsernameValidator

# Create your models here.
class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number = models.CharField("Номер телефона", max_length=30)
    adress = models.CharField("Адрес", max_length=250, blank=True, null=True)
    avatar = models.ImageField("Аватар", upload_to="user-ava/", null=True)
    
    def __str__(self): 
        return f'{self.user}'
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"