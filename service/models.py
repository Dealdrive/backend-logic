from django.db import models


# Create your models here.

def category_image_path(instance, filename):
    return 'image/cat/{}/{}'.format(instance.name, filename)

def package_image_path(instance, filename):
    return 'image/pak/{}/{}'.format(instance.name, filename)

class Category(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(upload_to= category_image_path, null=True, blank = True )
    discription = models.TextField(max_length=500, null=True, blank=True)
    # created = models.DateTimeField(auto_now_add=True,null=True, blank=True)

    # class Meta:
    #     # verbose_name_plural = "Categories"
    #     # ordering = ['created']

    def __str__(self):
        return self.name


class Package(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to= package_image_path, null=True, blank = True )
    price = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    category = models.ForeignKey(Category, related_name='package_category', on_delete=models.CASCADE)
    # created = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "Packages"
        # ordering = ['created']

    def __str__(self):
        return self.name