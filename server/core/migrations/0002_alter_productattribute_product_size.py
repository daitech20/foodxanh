# Generated by Django 4.1.4 on 2022-12-19 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productattribute',
            name='product_size',
            field=models.IntegerField(choices=[(0, '500gram'), (1, '1kg')]),
        ),
    ]