# Generated by Django 3.2.15 on 2022-09-06 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20220904_2239'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-id',), 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
    ]
