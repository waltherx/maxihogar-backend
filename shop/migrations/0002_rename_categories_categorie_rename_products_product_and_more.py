# Generated by Django 5.0.4 on 2024-05-05 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Categorie',
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
        migrations.RenameModel(
            old_name='Product_Attributes',
            new_name='Product_Attribute',
        ),
        migrations.RenameModel(
            old_name='Products_Skus',
            new_name='Products_Sku',
        ),
        migrations.RenameModel(
            old_name='Sub_Categories',
            new_name='Sub_Categorie',
        ),
    ]