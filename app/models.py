from tabnanny import verbose
from django.db import models
from django.core.files.storage import FileSystemStorage as FS


media_img = FS(location='app/static/app/media')


# Create your models here.


class categories(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'categories for nav items'
        verbose_name_plural = 'categories'


    def __str__(self):
        return '{} | {}'.format(self.id, self.name[:50])

class Products(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField('photo', storage=media_img)
    created = models.DateTimeField(auto_now=True)
    cat = models.ForeignKey(
        categories,
        on_delete=models.CASCADE,
        verbose_name = 'categories'
    )
    available = models.BooleanField('access', default=False)

    class Meta:
        verbose_name = 'products for the main page'
        verbose_name_plural = 'products'

    def __str__(self):
        return '{} | {}'.format(self.id, self.title[:100])

class Carousels(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField('image', storage = media_img)
    status = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = 'carpusels in the main page'
        verbose_name_plural = 'carousel'

    def __str__(self):
        return '{} | {}'.format(self.id, self.name)


class delivery(models.Model):
    title = models.CharField(max_length=200, blank=True)
    text = models.TextField(blank=True)

    class Meta:
        verbose_name = 'delivery data'
        verbose_name_plural = 'delivery info'

    def __str__(self):
        return '{} | {}'.format(self.id, self.title[:50])



class About(models.Model):
    text = models.TextField()


    def __str__(self):
        return 'about'