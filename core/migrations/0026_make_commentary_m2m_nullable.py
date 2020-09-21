# Generated by Django 3.1 on 2020-09-21 16:21

from django.db import migrations
import sortedm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_move_from_attribution_string_to_m2m'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vision',
            name='commentary_writers',
            field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, related_name='commentary_written_by', to='core.Writer'),
        ),
    ]