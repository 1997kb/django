# Generated by Django 3.2.5 on 2021-08-07 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='phone',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
