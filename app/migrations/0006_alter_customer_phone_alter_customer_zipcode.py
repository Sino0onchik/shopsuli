# Generated by Django 4.0.3 on 2022-04-24 19:47

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_customer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='zipcode',
            field=models.IntegerField(),
        ),
    ]
