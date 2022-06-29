from django.contrib import admin
from .models import Project
# Register your models here.

admin.site.register(Project)

# fields = ['image_tag']
# readonly_fields = ['image_tag']