from django.db import models
from realtors.models import Realtor


class Village(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    featured_image = models.ImageField(upload_to="villages", blank=True, default="default.jpg")
    direction = models.CharField(max_length=100)
    distance = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    square = models.IntegerField(default=0)
    land_price = models.IntegerField(default=0)
    contacts = models.CharField(max_length=200, blank=True)
    website = models.CharField(max_length=400, blank=True)
    vote_total = models.IntegerField(default=0)
    infrastructures = models.ManyToManyField('Infrastructure', blank=True)
    realtors = models.ManyToManyField(Realtor, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'посёлок'
        verbose_name_plural = "посёлки"


class Infrastructure(models.Model):
    name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'инфраструктуру'
        verbose_name_plural = 'инфраструктура'
