from django.db import models
from django.db.models.signals import post_save
# from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    last_name = models.CharField(max_length=255, verbose_name='Фамилия',
                                 null=True, blank=True)
    first_name = models.CharField(max_length=255, verbose_name='Имя',
                                  null=True, blank=True)
    middle_name = models.CharField(max_length=255, verbose_name='Отчество',
                                   null=True, blank=True)
    day_of_birthday = models.DateField(null=True, blank=True,
                                       verbose_name='День рождения')
    country = models.CharField(max_length=255, null=True, blank=True)

    USER_ROLES = [('user', 'Обычный пользователь'), ('support', 'Техподдержка'),
                  ('premium', 'Пользователь с подпиской')]

    email = models.EmailField(unique=True, null=True)
    user_role = models.CharField(max_length=20, choices=USER_ROLES,
                                 verbose_name='Роль пользователя',
                                 default=USER_ROLES[0][0])
    date_created = models.DateTimeField(auto_now_add=True,
                                        verbose_name='Дата создания',
                                        null=True)
    date_updated = models.DateTimeField(auto_now=True,
                                        verbose_name='Дата изменения',
                                        null=True)
    invite_counter = models.PositiveSmallIntegerField(default=0)

    is_agree_license = models.BooleanField(default=False)

    last_active_date = models.DateTimeField(null=True, blank=True,
                                            verbose_name='Дата и время последней активности')

    # invited_users = models.ManyToManyField(User, related_name='invited')
    SEX_ROLES = [('without', 'Пол не указан'),
                 ('man', 'Мужчина'),
                 ('woman', 'Женщина'), ]
    sex = models.CharField(max_length=20, choices=SEX_ROLES,
                           verbose_name='Пол пользователя',
                           default=SEX_ROLES[0][0])

    photo = models.ImageField("Изображение", upload_to="profiles/photos",
                              null=True,
                              default="profiles/photos/no-image-user.jpg")
    balance = models.DecimalField('Баланс', max_digits=6, decimal_places=2, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.middle_name}'


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)


class Asset(models.Model):
    icon = models.FileField("Изображение", upload_to="stocks_icon", null=True)
    name = models.CharField(max_length=255, verbose_name='Наименование актива',
                            null=True, blank=True)
    ticker = models.CharField(max_length=100, verbose_name='Тикер актива', null=True, blank=True, unique=True)
    price = models.DecimalField('Стоимость актива', max_digits=6, decimal_places=2)
    TYPES = [('no_type', ' Без типа'),
             ('Stock', 'акции/облигации'),
             ('Crypto', 'токен')]
    type = models.CharField(max_length=20, choices=TYPES,
                            verbose_name='Тип актива',
                            default=TYPES[0][0])
    price_json = models.JSONField(null=True, blank=True)
    sector = models.CharField(max_length=150, verbose_name='Сектор', null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='asset')
    statuses = [('in_processing', 'In processing'),
                ('bought', 'Bought'),
                ('sold', 'Sold'),
                ('failed', 'Failed')]
    status = models.CharField(max_length=20, choices=statuses,
                              verbose_name='Status',
                              default=statuses[0][0])
    purchase_price = models.DecimalField('Сумма', max_digits=6, decimal_places=2, null=True, default=0)
    count = models.FloatField(verbose_name='Количество')

    def __str__(self):
        return f'{self.user} {self.status} {self.count} {self.asset}'


class DealHistory(models.Model):
    time = models.TimeField(auto_now_add=True)
    items = models.OneToOneField(Item, verbose_name='Предметы сделки', related_name='deal_assets', null=True,
                                 on_delete=models.CASCADE)
    WHAT_HAPPEND = [('no_type', ' Без типа'),
                    ('buy_stock', 'Покупка акции/облигации'),
                    ('buy_crypto', 'Покупка токенизированных активов'),
                    ('sell_stock', 'Продажа акции/облигации'),
                    ('sell_crypto', 'Продажа токенизированных активов'),
                    ('exchange', 'Обмен')]
    deal_type = models.CharField(max_length=20, choices=WHAT_HAPPEND,
                                 verbose_name='Тип сделки',
                                 default=WHAT_HAPPEND[0][0])
    recipient = models.OneToOneField(User, verbose_name='Участник сделки',
                                     related_name='dealers', on_delete=models.CASCADE)
    deal_owner = models.OneToOneField(User, verbose_name='Иннициатор сделки',
                                      related_name='deal_owner', on_delete=models.CASCADE)
    price = models.DecimalField('Стоимость актива', max_digits=6, decimal_places=2)
