# Generated by Django 3.2 on 2021-05-01 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0005_sans_price_sans'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='phone_location',
            field=models.CharField(max_length=11, null=True, verbose_name='شماره تماس'),
        ),
    ]
