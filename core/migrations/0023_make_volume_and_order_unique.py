# Generated by Django 3.1 on 2020-09-12 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_vision_order_in_volume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vision',
            name='order_in_volume',
            field=models.IntegerField(),
        ),
        migrations.AddConstraint(
            model_name='vision',
            constraint=models.UniqueConstraint(fields=('volume', 'order_in_volume'), name='unique_volume_and_order'),
        ),
    ]
