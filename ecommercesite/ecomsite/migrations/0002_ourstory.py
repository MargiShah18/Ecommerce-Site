# Generated by Django 4.0.4 on 2022-06-08 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ourstory',
            fields=[
                ('ostory_id', models.AutoField(primary_key=True, serialize=False)),
                ('ostory_curcive_text', models.CharField(max_length=50)),
                ('ostory_bold_text', models.CharField(max_length=50)),
                ('ostory_p1', models.CharField(max_length=200)),
                ('ostory_p2', models.CharField(max_length=200)),
            ],
        ),
    ]