# Generated by Django 3.1.8 on 2021-07-31 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0008_auto_20210731_0831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='info',
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='profile',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения'),
        ),
        migrations.AddField(
            model_name='profile',
            name='day_of_birthday',
            field=models.DateField(blank=True, null=True, verbose_name='День рождения'),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='profile',
            name='invite_counter',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_agree_license',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_active_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата и время последней активности'),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия'),
        ),
        migrations.AddField(
            model_name='profile',
            name='middle_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Отчество'),
        ),
        migrations.AddField(
            model_name='profile',
            name='sex',
            field=models.CharField(choices=[('without', 'Пол не указан'), ('man', 'Мужчина'), ('woman', 'Женщина')], default='without', max_length=20, verbose_name='Пол пользователя'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user_role',
            field=models.CharField(choices=[('user', 'Обычный пользователь'), ('support', 'Техподдержка'), ('premium', 'Пользователь с подпиской')], default='user', max_length=20, verbose_name='Роль пользователя'),
        ),
        migrations.DeleteModel(
            name='ProfileInfo',
        ),
    ]