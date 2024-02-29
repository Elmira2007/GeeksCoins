from typing import Iterable
from django.db import models

from apps.users.models import User
# Create your models here.

class Transactions(models.Model):
    from_user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'from_user')
    to_user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'to_user')
    amout = models.ImageField()
    created_at = models.DateTimeField(auto_now_add = True)
    is_completed = models.BooleanField(default = False)
    
    def save(self, *args, **kwargs):
        if self.is_completed:
            raise ValueError("Транзакция уже завершена")
        
        if not self.is_completed:
            from_user_balance = self.from_user.balance
            to_user_wallet_adress = self.to_user.wallet_adress
            
            if from_user_balance >= self.amout:
                self.from_user.balance -= self.amout
                self.to_user.wallet_adress += self.amout
                
                self.is_completed = True
                
                self.from_user.save()
                self.to_user.save()
                super(Transactions, self).save(*args, **kwargs)
            else:
                raise ValueError("Недостаточно средств для транзакции!")
            
    class Meta:
        verbose_name = "Транзакция"
        verbose_name_plural = "Транзакции"