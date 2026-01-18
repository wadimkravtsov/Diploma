from django.contrib import admin
from .models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'first_name', 'last_name', 'email', 'phone', 'username', 'realt')
    list_display_links = ('first_name', 'last_name', 'realt')
    search_fields = ('first_name', 'last_name')

admin.site.register(Profile,ProfileAdmin)
