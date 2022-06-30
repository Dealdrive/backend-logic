from rest_framework import serializers
from .models import Category,Package



class DetailedPackageSerializer(serializers.ModelSerializer):
    category  =serializers.CharField(source = "category.categoryName", read_only = True)


    class Meta:
        model = Package
        fields = ['id','packageName', 'price', 'description', 'image', 'category']


class PackageSerializer(serializers.ModelSerializer):
    # category  =serializers.CharField(source = "category.name", read_only = True)


    

    class Meta:
        model = Package
        fields = ['id','packageName', 'price', 'description', 'image', 'category']

        # def get_category(self, obj):
        #     return obj.category.name




class CategorySerializer(serializers.ModelSerializer):
    package_category = PackageSerializer(many = True)
    

    
    class Meta:
        model = Category
        fields = ['id','categoryName','discription', 'image', 'package_category']

   

