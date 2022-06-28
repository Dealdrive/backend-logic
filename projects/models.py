from django.db import models


def project_image_path(instance, filename):
    return 'image/pro/{}/{}'.format(instance.pro_title, filename)


class Project(models.Model):
    pro_title = models.CharField(max_length=250)
    pro_link = models.CharField(max_length=250)
    img = models.ImageField(upload_to = project_image_path, blank=False, null=False)
    # created = models.DateTimeField(auto_now_add=True,null=True, blank=True)

    class Meta:
        # ordering = ['created']
         verbose_name_plural = "Projects"

    def __str__(self):
        return self.pro_title