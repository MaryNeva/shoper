from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Catalog_section(models.Model):
    name_section = models.CharField(max_length=50)
    slug = models.SlugField(default='', null=False, db_index=True)
    name_ru = models.CharField(max_length=50, blank=True, null=True)

   # class Meta:
   #     ordering = ('name_section',)
   #     verbose_name = 'Категория'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name_section)
        super(Catalog_section, self).save(*args, **kwargs)

    def get_section_url(self):
        return reverse('section-detail', args=[self.slug])

    def __str__(self):
        return f'{self.name_section} '

class Units(models.Model):
    name_unit = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.name_unit}'

class Product(models.Model):
    #UNIT_CHOICES = [('kg', 'kilogram'),
    #             ('gr', 'gram'),
    #             ('l', 'litre'),
    #             ('ml', 'milliliter'),
    #             ('pkg', 'package'),
    #             ('unit', 'unit')]

    name = models.CharField(max_length=100)
    name_unit = models.ForeignKey(Units, on_delete=models.SET_NULL, null=True)
    counting = models.IntegerField(default=0)
    comment = models.CharField(max_length=200, null=True, blank=True)
    section = models.ForeignKey(Catalog_section, on_delete=models.SET_NULL, null=True )
    slug = models.SlugField(default='', null=False)
    name_ru = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ('name', 'counting', 'name_unit',)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_products_url(self):
        return reverse('section-detail/product-detail', args=[self.slug, Catalog_section.slug])


class Login(models.Model):
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    nickname = models.CharField(max_length=15)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)


