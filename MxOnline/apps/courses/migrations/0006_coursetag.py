# Generated by Django 4.1.7 on 2023-04-24 11:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_course_org'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add time')),
                ('tag', models.CharField(max_length=100, verbose_name='Tag Name')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='Course')),
            ],
            options={
                'verbose_name': '课程标签',
                'verbose_name_plural': '课程标签',
            },
        ),
    ]
