# Generated by Django 4.1.7 on 2023-04-12 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0004_alter_courseorg_is_auth_alter_courseorg_is_gold'),
        ('courses', '0004_alter_course_options_alter_courseresource_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organizations.courseorg', verbose_name='Course Organization'),
        ),
    ]