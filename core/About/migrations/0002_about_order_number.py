# Generated by Django 3.2.12 on 2022-03-12 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='order_number',
            field=models.IntegerField(null=True),
        ),
    ]
