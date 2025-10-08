from tkinter.constants import CASCADE

from django.db import models


class Realtor(models.Model):
    title = models.CharField(max_length=100)
    office_adress = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    featured_image = models.ImageField(upload_to="realtors", blank=True, default="default.jpg")
    experience = models.IntegerField(default=0)
    contacts = models.CharField(max_length=200, blank=True)
    website = models.CharField(max_length=400, blank=True)
    whatsapp = models.CharField(max_length=100, blank=True)
    telegram = models.CharField(max_length=100, blank=True)
    # villages = models.ManyToManyField(Village, blank=True)



    def __str__(self):
        return self.title

class Cottage(models.Model):
    rlt = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    village = models.CharField(max_length=100)
    adress = models.CharField(max_length=200)
    land_area = models.IntegerField(default=0)
    house_area = models.IntegerField(default=0)
    floors = models.IntegerField(default=1)
    walls = models.CharField(max_length=100)
    bedrooms = models.IntegerField(default=1)
    web_site = models.CharField(max_length=200, blank=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.adress

