# Generated by Django 3.0.8 on 2020-08-16 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_volume_date_season'),
    ]

    operations = [
        migrations.AddField(
            model_name='volume',
            name='date_year',
            field=models.IntegerField(default=0),
        ),
    ]
