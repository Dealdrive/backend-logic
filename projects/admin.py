from django.contrib import admin
from .models import Project
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('pro_title', 'pro_link', 'img')


admin.site.register(Project, ProjectAdmin)



# fields = ['image_tag']
# readonly_fields = ['image_tag']