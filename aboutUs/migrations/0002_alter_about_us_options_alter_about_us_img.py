# Generated by Django 4.0.5 on 2022-06-29 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutUs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about_us',
            options={'verbose_name_plural': 'About_Us'},
        ),
        migrations.AlterField(
            model_name='about_us',
            name='img',
            field=models.ImageField(upload_to='image/about'),
        ),
    ]