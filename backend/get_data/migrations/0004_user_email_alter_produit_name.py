# Generated by Django 5.1.6 on 2025-03-17 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_data', '0003_remove_facture_products_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(blank=True, max_length=300, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
