# Generated by Django 4.0.4 on 2022-06-22 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomsite', '0027_suppliers_delete_homeproducts'),
    ]

    operations = [

        migrations.AlterField(
            model_name='products',
            name='pr_supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecomsite.suppliers'),
        ),
    ]
