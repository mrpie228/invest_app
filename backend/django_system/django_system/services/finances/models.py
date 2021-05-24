from django.db import models

from login_system.models import Profile, User


# Create your models here.
class Asset(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование актива',
                            null=True, blank=True)
    ticker = models.CharField(max_length=100, verbose_name='Тикер актива', null=True, blank=True)
    price = models.DecimalField('Стоимость актива', max_digits=6, decimal_places=2)
    count = models.PositiveIntegerField(verbose_name='Количество')


class Portfolio(models.Model):
    assets = models.ManyToManyField(Asset, verbose_name='Активы', related_name='assets', null=True)
    profile = models.ManyToManyField(Profile, verbose_name='Профиль',
                                     related_name='profile')
    sum = models.DecimalField('Сумма', max_digits=6, decimal_places=2)

    def get_sum(self):
        for asset in self.assets:
            all_price = asset.price + all_price
        self.sum = all_price
        self.save()
        return all_price


class DealHistory(models.Model):
    time = models.TimeField(auto_now_add=True)
    WHAT_HAPPEND = [('no_type', ' Без типа'),
                    ('buy_stock', 'Покупка акции/облигации'),
                    ('buy_crypto', 'Покупка токенизированных активов'),
                    ('sell_stock', 'Продажа акции/облигации'),
                    ('sell_crypto', 'Продажа токенизированных активов'),
                    ('exchange', 'Обмен')]
    deal_type = models.CharField(max_length=20, choices=WHAT_HAPPEND,
                                 verbose_name='Тип сделки',
                                 default=WHAT_HAPPEND[0][0])
    dealers = models.ManyToManyField(User, verbose_name='Участник(и) сделки',
                                     related_name='dealers')
    deal_owner = models.ManyToManyField(User, verbose_name='Участник(и) сделки',
                                        related_name='deal_owner')
    price = models.DecimalField('Стоимость актива', max_digits=6, decimal_places=2)

# class Commision(models.Model):
#     percent = models.DecimalField('Процент коммисии',)
