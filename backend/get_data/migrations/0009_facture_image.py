# Generated by Django 5.1.6 on 2025-03-20 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_data', '0008_facture_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='facture',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
