from dataclasses import fields
from rest_framework import serializers
from .models import Services



# class DetailedPackageSerializer(serializers.ModelSerializer):
#     Services  =serializers.CharField(source = "services.servicesName", read_only = True)


#     class Meta:
#         model = Package
#         fields = ['id','packageName', 'price', 'description', 'image', 'Services']


# class PackageSerializer(serializers.ModelSerializer):
#     # Services  =serializers.CharField(source = "Services.name", read_only = True)


#     class Meta:
#         model = Package
#         fields = ['id','packageName', 'price', 'description', 'image', 'services']

#         # def get_Services(self, obj):
#         #     return obj.Services.name

#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         data = serializers.ModelSerializer.to_representation(self, instance)
#         return data




class ServicesSerializer(serializers.ModelSerializer):
    # package_services = PackageSerializer(many = True, read_only = True)
    

    
    class Meta:
        model = Services
        # read_only_fields = ('id','servicesName','discription', 'image', 'package_services')
        # fields = ['id','servicesName','discription', 'image', 'package_services']
        fields = '__all__'


    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data = serializers.ModelSerializer.to_representation(self, instance)
    #     return data

   

