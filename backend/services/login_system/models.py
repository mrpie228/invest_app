from django.db import models

from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    photo = models.ImageField("Изображение", upload_to="profiles/photos", null=True,
                              default="profiles/photos/no-image-user.jpg")

    class Meta:
        verbose_name = "Профиль"
        verbose_name = "Профили"


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)
