# Generated by Django 3.2.15 on 2022-09-06 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
    ]
