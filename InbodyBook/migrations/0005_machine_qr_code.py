# Generated by Django 3.2.8 on 2021-12-15 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InbodyBook', '0004_rename_meachines_machine'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='qr_code',
            field=models.ImageField(default='non.png', upload_to='images/machine_qr_code'),
        ),
    ]
