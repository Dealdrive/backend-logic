# Generated by Django 4.0.5 on 2022-07-01 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='discription',
        ),
        migrations.AddField(
            model_name='services',
            name='List1',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
