from django.contrib import admin
from .models import About_Us
# Register your models here.


class About_UsAdmin(admin.ModelAdmin):
    list_display = ('body', 'img')


admin.site.register(About_Us, About_UsAdmin)