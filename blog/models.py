import uuid
from django.db import models


def blog_image_path(instance, filename):
    return 'image/blog/{}/{}'.format(instance.topic, filename)


class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    topic = models.CharField(max_length=250)
    intro = models.TextField(max_length=800)
    main = models.TextField(max_length=800)
    img = models.ImageField(upload_to = blog_image_path, blank=False, null=False)
    # created = models.DateTimeField(auto_now_add=True,null=True, blank=True)


    class Meta:
        # ordering = ['created']
         verbose_name_plural = "Blogs"

    def __str__(self):
        return self.topic