# Generated by Django 4.0.4 on 2022-04-27 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='companies_shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_name', models.CharField(max_length=50)),
                ('comp_address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='product_types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_type_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_photo', models.FileField(blank=True, null=True, upload_to='uploads/products_and_services_photos/')),
                ('prod_name', models.CharField(max_length=50)),
                ('prod_desc', models.CharField(max_length=255)),
                ('company_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='product_types_companies_shop', to='backend.companies_shop')),
                ('product_types_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='products_product_types', to='backend.product_types')),
            ],
        ),
        migrations.CreateModel(
            name='product_photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('multi_prod_photo', models.FileField(blank=True, null=True, upload_to='uploads/products_and_services_photos/')),
                ('product_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='product_photos_products', to='backend.products')),
            ],
        ),
    ]
