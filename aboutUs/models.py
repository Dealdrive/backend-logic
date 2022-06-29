import uuid
from django.db import models

# Create your models here.

def about_image_path(instance, filename):
    return 'image/about/{}/{}'.format(instance, filename)

class About_Us(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField(max_length=5000)
    img = models.ImageField(upload_to = "image/about", blank=False, null=False)
    # created = models.DateTimeField(auto_now_add=True,)


    class Meta:
        # ordering = ['created']
         verbose_name_plural = "About_Us"

    def __str__(self):
        return self.body