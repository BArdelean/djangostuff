# Generated by Django 2.2 on 2019-04-14 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tanks', '0002_auto_20190415_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tank',
            name='barrel_caliber',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='tank',
            name='turret_caliber',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4),
        ),
    ]
