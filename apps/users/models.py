from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(
        max_length = 255,
        verbose_name = "Номер телефона"
    )
    age = models.PositiveIntegerField(
        verbose_name = "Возраст студента",
        blank=True, null=True
    )
    balance = models.PositiveIntegerField(
        verbose_name = "Баланс студента",
        default = 4
    )
    direction = models.CharField(
        max_length = 255,
        verbose_name = "Направление"
    )
    wallet_address = models.CharField(
        max_length =255,
        verbose_name = "Кошелёк",
        default = '4',
        blank=True, null=True
    )
    
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class UserCoins(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_coins')
    balance = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Coin Info"

    class Meta:
        verbose_name = 'Коин'
        verbose_name_plural = 'Коины'
