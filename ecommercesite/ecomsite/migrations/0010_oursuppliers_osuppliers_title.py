# Generated by Django 4.0.4 on 2022-06-08 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomsite', '0009_oursuppliers'),
    ]

    operations = [
        migrations.AddField(
            model_name='oursuppliers',
            name='osuppliers_title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
