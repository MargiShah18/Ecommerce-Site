# Generated by Django 4.0.4 on 2022-06-27 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomsite', '0029_delete_homeproducts_registeruser_city1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(default='', max_length=100)),
                ('product_id', models.CharField(default='', max_length=100)),
                ('quantity', models.CharField(default='', max_length=100)),
            ],
        )
    ]
