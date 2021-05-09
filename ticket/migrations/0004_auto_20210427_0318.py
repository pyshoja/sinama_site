# Generated by Django 3.2 on 2021-04-26 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_auto_20210427_0257'),
    ]

    operations = [
        migrations.AddField(
            model_name='sans',
            name='film_sans',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ticket.film', verbose_name='فیلم سانس'),
        ),
        migrations.AlterField(
            model_name='sans',
            name='local_sans',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ticket.location', verbose_name='مکان سانس'),
        ),
    ]