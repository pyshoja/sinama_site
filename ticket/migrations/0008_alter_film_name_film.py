# Generated by Django 3.2 on 2021-05-01 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0007_alter_film_name_film'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='name_film',
            field=models.CharField(max_length=200, verbose_name='نام فیلم'),
        ),
    ]
