from django.db import models
# from login_system.models import Profile


# Create your models here.
class Asset(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование актива',
                            null=True, blank=True)
    price = models.DecimalField('Стоимость актива', max_digits=6, decimal_places=2)


class Portfolio(models.Model):
    assets = models.ManyToManyField(Asset, on_delete=models.DO_NOTHING, verbose_name='Активы', related_name='assets')
    # profile = models.ManyToManyField(Profile, on_delete=models.DO_NOTHING, verbose_name='Профиль',
    #                                  related_name='profile')
    sum = models.DecimalField('Сумма', max_digits=6, decimal_places=2)

