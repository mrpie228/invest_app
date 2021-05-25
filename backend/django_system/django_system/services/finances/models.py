from django.db import models

from login_system.models import Profile, User


# Create your models here.
class Asset(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование актива',
                            null=True, blank=True)
    ticker = models.CharField(max_length=100, verbose_name='Тикер актива', null=True, blank=True, unique=True)
    price = models.DecimalField('Стоимость актива', max_digits=6, decimal_places=2)
    TYPES = [('no_type', ' Без типа'),
             ('stock', 'акции/облигации'),
             ('crypto', 'токен')]
    type = models.CharField(max_length=20, choices=TYPES,
                            verbose_name='Тип актива',
                            default=TYPES[0][0])
    def __str__(self):
        return self.name

class Item(models.Model):
    asset = models.OneToOneField(Asset, on_delete=models.DO_NOTHING)
    # if asset.type == 'stock' or asset.type == 'no_type':
    #     count = models.PositiveIntegerField(verbose_name='Количество')
    # else:
    count = models.FloatField(verbose_name='Количество ')


class Portfolio(models.Model):
    items = models.ManyToManyField(Item, verbose_name='Активы', related_name='assets', null=True)
    profile = models.ManyToManyField(Profile, verbose_name='Профиль',
                                     related_name='profile')
    sum = models.DecimalField('Сумма', max_digits=6, decimal_places=2)


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
