# Generated by Django 4.1.6 on 2023-02-13 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='amount',
            field=models.IntegerField(),
        ),
    ]
