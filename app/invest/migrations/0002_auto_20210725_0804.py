# Generated by Django 3.1.8 on 2021-07-25 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя')),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Отчество')),
                ('day_of_birthday', models.DateField(blank=True, null=True, verbose_name='День рождения')),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('user_role', models.CharField(choices=[('user', 'Обычный пользователь'), ('support', 'Техподдержка'), ('premium', 'Пользователь с подпиской')], default='user', max_length=20, verbose_name='Роль пользователя')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('date_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('invite_counter', models.PositiveSmallIntegerField(default=0)),
                ('is_agree_license', models.BooleanField(default=False)),
                ('last_active_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата и время последней активности')),
                ('sex', models.CharField(choices=[('user', 'Обычный пользователь'), ('support', 'Техподдержка'), ('premium', 'Пользователь с подпиской')], default='without', max_length=20, verbose_name='Пол пользователя')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='profile',
            name='info',
            field=models.OneToOneField(default=123, on_delete=django.db.models.deletion.CASCADE, to='invest.profileinfo'),
            preserve_default=False,
        ),
    ]
