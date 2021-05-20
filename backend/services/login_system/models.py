from django.db import models

from django.db.models.signals import post_save
# from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser

MAX_COMPANY_AVATAR_SIZE = 2097152


class User(AbstractUser):
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
    SEX_ROLES = [('man', 'Мужчина'), ('woman', 'Женщина'), ]
    sex = models.CharField(max_length=20, choices=USER_ROLES,
                           verbose_name='Пол пользователя',
                           default=SEX_ROLES[0][0])

    auth_key = models.TextField(blank=True, verbose_name="Ключ авторизации")

    is_auth_key = models.BooleanField(
        default=False, verbose_name='Может ли пользователь использовать ключ авторизации'
    )

    def get_user_name(self):
        return self.username

    def __str__(self):
        return f'{self.username}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    photo = models.ImageField("Изображение", max_file_size=MAX_COMPANY_AVATAR_SIZE, upload_to="profiles/photos",
                              null=True,
                              default="profiles/photos/no-image-user.jpg")
    balance = models.DecimalField('Баланс', max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = "Профиль"
        verbose_name = "Профили"


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)
