# Generated by Django 3.0.5 on 2020-05-04 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webinar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='justuser',
            name='just_id',
            field=models.CharField(default='e1bf7aee-000e-4066-8afa-93138293f51c', max_length=100),
        ),
    ]
