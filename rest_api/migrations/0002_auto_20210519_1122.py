# Generated by Django 3.2 on 2021-05-19 06:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rest_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='testrest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='متن ')),
                ('link', models.URLField(verbose_name='لینک ')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده ')),
            ],
            options={
                'verbose_name': 'تست اپلیکیشن',
                'verbose_name_plural': 'تست اپلیکیشن',
            },
        ),
        migrations.DeleteModel(
            name='test',
        ),
    ]