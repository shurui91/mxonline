# Generated by Django 4.1.7 on 2023-04-27 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_userprofile_first_name_alter_userprofile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='discord.png', upload_to='head_image/%Y/%m', verbose_name='Avatar/头像'),
        ),
    ]
