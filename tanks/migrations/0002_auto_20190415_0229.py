# Generated by Django 2.2 on 2019-04-14 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tanks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tank',
            name='turret_caliber',
            field=models.FloatField(),
        ),
    ]
