# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-20 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ro_app', '0017_auto_20171218_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAlert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Укажите заголовок для уведомления. Он будет являться темой электронного письма', max_length=100, verbose_name='Заголовок уведомления')),
                ('message', models.CharField(help_text='Тело сообщения уведомления. Максимум 500 символов', max_length=500, verbose_name='Сообщение')),
                ('image', models.ImageField(blank=True, default=None, help_text='Рекомендуемый размер изображения - 640 на 400 пикселей до 1 мегабйта. В противном случае возможны перебои доставки, связанные с ограничениями почтовых клиентов', null=True, upload_to='images/user_alerts_images/', verbose_name='Прикрепленное изображение')),
            ],
            options={
                'verbose_name': 'Уведомление для подписчиков',
                'verbose_name_plural': 'Уведомления для подписчиков',
            },
        ),
        migrations.AlterModelOptions(
            name='operatormail',
            options={'verbose_name': ('Электронный адрес для уведомлений',), 'verbose_name_plural': 'Список электроных адресов для уведомлений'},
        ),
    ]
