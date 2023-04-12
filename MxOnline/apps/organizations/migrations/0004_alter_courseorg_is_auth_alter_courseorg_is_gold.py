# Generated by Django 4.1.7 on 2023-04-12 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0003_alter_city_options_alter_courseorg_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorg',
            name='is_auth',
            field=models.BooleanField(default=False, verbose_name='Is this an authenticated organization?'),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='is_gold',
            field=models.BooleanField(default=False, verbose_name='Is this a golden organization?'),
        ),
    ]
