# Generated by Django 4.0.3 on 2022-03-23 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
