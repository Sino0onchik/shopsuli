# Generated by Django 4.0.4 on 2022-05-24 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderplaced',
            name='invoice',
            field=models.FileField(null=True, upload_to='invoice'),
        ),
    ]
