from django_cron import CronJobBase, Schedule
from apps.users.models import User
from datetime import timedelta
import logging
from django.utils import timezone  

class CoinCronJob(CronJobBase):
    RUN_EVERY_DAYS = 30  
    schedule = Schedule(run_every_days=RUN_EVERY_DAYS)
    code = 'coins.CoinCronJob' 

    def do(self):  
        try:
            user_coins_list = User.objects.all()
            for user_coins in user_coins_list:
                if user_coins.balance >= 4:
                    user_coins.balance -= 4
                    user_coins.save()
                else:
                    user_coins.balance = 0
                    user_coins.save()
                    
            logging.info("CoinCronJob выполнена успешно")
        except Exception as e:
            logging.error(f"Ошибка выполнения CoinCronJob: {str(e)}")