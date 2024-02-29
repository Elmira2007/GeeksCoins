from django.db import models
from apps.users.models import User  

# Create your models here.
class UserCoins(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name ='coins')
    balance = models.PositiveIntegerField(default = 0)
    last_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.user.username} информация о монете"

    class Meta:
        verbose_name = 'Коин'
        verbose_name_plural = 'Коины' 

