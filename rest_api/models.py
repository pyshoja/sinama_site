from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class testrest (models.Model):
    class Meta:
        verbose_name = 'تست اپلیکیشن'
        verbose_name_plural = 'تست اپلیکیشن'

    title =models.CharField(max_length=50 , verbose_name='متن ')
    link =models.URLField(verbose_name='لینک ')
    writer =models.ForeignKey(User , on_delete=models.CASCADE , verbose_name='نویسنده ')

    def __str__(self):
        return self.title


