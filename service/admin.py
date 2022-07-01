from django.contrib import admin
from .models import Services
# Register your models here.


# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('servicesName', 'servicesList1', 'servicesList2', 'servicesList3', 'servicesList5')


# admin.site.register(Services)
# admin.site.register(Package)

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('servicesName', 'image', 'servicesList1', 'servicesList2', 'servicesList3', 'servicesList5')


admin.site.register(Services, ServicesAdmin)
