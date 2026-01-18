from django.contrib import admin

from .models import Realtor, Cottage

class CottageAdmin(admin.ModelAdmin):
    list_display = ('id','rlt', 'village', 'adress', 'land_area', 'house_area', 'floors', 'bedrooms', 'price')
    list_display_links = ('id', 'village', 'adress')
    search_fields = ('village', 'adress')

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'office_adress', 'contacts')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'office_adress')

admin.site.register(Realtor,RealtorAdmin)
admin.site.register(Cottage, CottageAdmin)


