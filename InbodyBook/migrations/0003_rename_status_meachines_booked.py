# Generated by Django 3.2.8 on 2021-11-14 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InbodyBook', '0002_remove_institution_region'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meachines',
            old_name='status',
            new_name='booked',
        ),
    ]
