from django.db import models
from django.urls import reverse
# Create your models here.


class CategoryEquipments(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Категроии оборудования'
        verbose_name_plural = 'Категории оборудования'
        ordering = ['name']

    def __str__(self):
        return self.name


class Equipments(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название оборудования', db_index=True)
    cat = models.ForeignKey('CategoryEquipments', on_delete=models.PROTECT, verbose_name='Категория')

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'
        ordering = ['name']

    def __str__(self):
        return self.name


CHOICE = Equipments.objects.all()


class Events(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название мероприятия', db_index=True)
    data_begin = models.DateTimeField(verbose_name='Начало мероприятия')
    data_end = models.DateTimeField(verbose_name='Конец мероприятия')
    slug = models.SlugField(unique=True, db_index=True, max_length=255)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    list_eq2 = models.ManyToManyField('Equipments', verbose_name='Оборудование',)

    class Meta:
        verbose_name = 'Мероприятия'
        verbose_name_plural = 'Мероприятия'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('event', kwargs={'event_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Категроии'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name



