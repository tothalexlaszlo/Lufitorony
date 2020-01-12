from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField('Név', max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Kategória'
        verbose_name_plural = 'Kategóriák'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Kategória')
    name = models.CharField('Név', max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField('Kép', upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField('Leírás', blank=True)
    price = models.DecimalField('Ár', max_digits=10, decimal_places=0)
    available = models.BooleanField('Elérhető', default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
