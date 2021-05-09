from django.db import models



# Create your models here.

class Janer(models.Model):
    class Meta:
        verbose_name = 'ژانر ها'
        verbose_name_plural = 'ژانر ها'

    janer_name = models.CharField(max_length=200, verbose_name='نوع ژانر')
    janer_tozihat = models.CharField(max_length=200, verbose_name='معرفی ژانر')
    image_janer = models.ImageField(upload_to='janerimages', verbose_name='عکس ژانر', null=True)

    def __str__(self):
        return self.janer_name


class Film(models.Model):
    class Meta:
        verbose_name = 'فیلم ها'
        verbose_name_plural = 'فیلم ها'

    namber_film = models.CharField(max_length=100, null=True, verbose_name='سریال فیلم')
    name_janer = models.ForeignKey(to=Janer, on_delete=models.PROTECT, null=True, verbose_name='نوع ژانر')
    name_film = models.CharField(max_length=200, verbose_name='نام فیلم')
    karghardan=models.CharField(max_length=50,null=True,verbose_name=' کارگردان')
    name_bazigaran = models.CharField(max_length=200, verbose_name='نام بازیگران')
    tozihat = models.CharField(max_length=1000, verbose_name='درباره فیلم')
    time_film = models.DateField(null=True , verbose_name='سال تولید فیلم')
    image_film = models.ImageField(upload_to='filmimages', verbose_name='عکس فیلم', null=True)
    film_time= models.CharField(max_length=100 , null=True , verbose_name='تایم فیلم')
    country_film = models.CharField(max_length=50 ,null=True , verbose_name='محصول کشور')
    z0= 1
    z9= 2
    z14=3
    z18=4
    z50=5
    z5=6
    age_choise = ((z0 , 'مناسب برای تمام سنین'),
                  (z5 , 'مناسب برای کودکان زیر 9 سال'),
                  (z9 , 'تماشا افراد زیر 9 سال ممنوع است'),
                  (z14 , 'تماشا افراد زیر 14 سال ممنوع است'),
                  (z18 , 'مناسب برای افراد بالای 18 سال'),
                  (z50 , 'تماشا برای افرادی که ناراحتی قلبی دارند ممنوع است'))
    age_film = models.IntegerField(choices=age_choise ,null=True , verbose_name='محدودیت های تماشا فیلم')


    def __str__(self):
        return self.name_film



class Location (models.Model):
    class Meta:
        verbose_name = 'سینما ها'
        verbose_name_plural = 'سینما ها'
    a=1 ; b=2 ; c=3 ; d=4 ; e=5 ; f=6 ; g=7 ; h=8 ; i=9 ; j=10 ; k=11 ; l=12 ; m=13 ; n=14 ; o=15 ; p=16 ; q=17 ; r=18 ; s=19 ; t=20 ; u=21 ; v=22 ; w=23 ; x=24 ; y=25 ; z=26 ; aa=27 ; bb=28 ; cc=29 ; dd=30 ; ee=31
    ostan_choises = ((d , 'اصفهان'),(h , 'تهران'),(k , 'مشهد'),(q , 'شیراز'),(s , 'قم'),(bb , 'مرکزی'))
    ostan=models.IntegerField(choices=ostan_choises , verbose_name='استان ها')
    name_location=models.CharField(max_length=100, verbose_name='نام سینما')
    adress_location=models.CharField(max_length=300 , verbose_name='ادرس سینما')
    phone_location=models.CharField(max_length=11 , null=True, verbose_name='شماره تماس')

    def __str__(self):
        return '{} {}'.format (self.name_location,self.adress_location)




class sans(models.Model):
    class Meta:
        verbose_name = 'سانس ها'
        verbose_name_plural = 'سانس ها'

    namber_sans = models.CharField(max_length=100, null=True, verbose_name='سریال سانس')
    film_sans = models.ForeignKey(to=Film, on_delete=models.PROTECT, null=True, verbose_name='فیلم سانس')
    time_sans = models.DateTimeField(verbose_name='زمان سانس')
    local_sans = models.ForeignKey(to= Location, on_delete=models.PROTECT, null=True , verbose_name='مکان سانس')
    start = 1
    end = 2
    blit = 3
    kansel= 4
    endblit= 5
    status_choices = ((start, ' سانس شروع شده است'),
                      (end, ' سانس تمام شده است'),
                      (blit, 'در حال فروش بلیط'),
                      (kansel, ' سانس کنسل شده است'),
                      (endblit, 'بلیط تمام شده است'))
    status_sans = models.IntegerField(choices=status_choices, verbose_name='وضعیت سانس')
    zarfiat_sans = models.IntegerField(verbose_name='ظرفیت سانس')
    price_sans = models.CharField(max_length=30,default='تومان' , verbose_name= 'هزینه سانس',null=True)

    def __str__(self):
        return '{} {}'.format (self.film_sans,self.local_sans)



class Profile(models.Model):
    class Meta:
        verbose_name = 'پروفایل ها'
        verbose_name_plural = 'پروفایل ها'

    first_name = models.CharField(max_length=100, verbose_name='نام')
    last_name = models.CharField(max_length=100, verbose_name='نام خانوادگی')
    Man = 1
    Male = 2
    jns_choices = ((Man, "مرد"),
                   (Male, "زن"))
    jens = models.IntegerField(choices=jns_choices, verbose_name='جنسیت', null=True)
    imail_name = models.CharField(max_length=100, null=True, verbose_name='ایمیل')
    adress_name = models.CharField(max_length=200, verbose_name='آدرس محل سکونت')
    phone_name = models.CharField(max_length=11, default='09', verbose_name='شماره تماس')
    image_name = models.ImageField(upload_to='profileimages', verbose_name='عکس پروفایل', null=True)

    def __str__(self):
        return self.imail_name

