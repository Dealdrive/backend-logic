from django.db import models


# Create your models here.

def serv_image_path(instance, filename):
    return 'image/serv/{}/{}'.format(instance.name, filename)

def package_image_path(instance, filename):
    return 'image/pak/{}/{}'.format(instance.name, filename)

class Services(models.Model):
    servicesName = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(upload_to= 'image/serv', null=True, blank = True )
    servicesList1 = models.TextField(max_length=500, null=True, blank=True)
    servicesList2 = models.TextField(max_length=500, null=True, blank=True)
    servicesList3 = models.TextField(max_length=500, null=True, blank=True)
    servicesList4 = models.TextField(max_length=500, null=True, blank=True)
    servicesList5 = models.TextField(max_length=500, null=True, blank=True)
  

    # class Meta:
    #     # verbose_name_plural = "Categories"
    #     # ordering = ['created']

    def __str__(self):
        return self.servicesName


# class Package(models.Model):
#     packageName = models.CharField(max_length=250)
#     image = models.ImageField(upload_to= 'image/serv', null=True, blank = True )
#     price = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
#     description = models.TextField(max_length=500, null=True, blank=True)
#     services = models.ForeignKey(Services, related_name='package_services', on_delete=models.CASCADE)
#     # created = models.DateTimeField(auto_now_add=True)


#     # class Meta:
#     #     verbose_name_plural = "Packages"
#         # ordering = ['created']

#     def __str__(self):
#         return self.packageName