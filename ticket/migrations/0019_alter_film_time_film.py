# Generated by Django 3.2 on 2021-05-18 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0018_alter_film_time_film'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='time_film',
            field=models.DateField(null=True, verbose_name='زمان تولید فیلم'),
        ),
    ]