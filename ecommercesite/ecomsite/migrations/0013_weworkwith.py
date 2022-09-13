# Generated by Django 4.0.4 on 2022-06-08 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomsite', '0012_homesoldproducts'),
    ]

    operations = [
        migrations.CreateModel(
            name='weworkwith',
            fields=[
                ('www_id', models.AutoField(primary_key=True, serialize=False)),
                ('www_title', models.CharField(default='', max_length=100)),
                ('www_image', models.ImageField(default='', upload_to='ecomsite/images')),
            ],
        ),
    ]
