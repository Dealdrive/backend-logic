# Generated by Django 4.0.5 on 2022-06-29 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutUs', '0004_alter_about_us_id_alter_about_us_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_us',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
