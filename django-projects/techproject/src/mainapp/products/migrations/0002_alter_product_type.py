# Generated by Django 4.1 on 2022-08-05 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('entrees', 'entrees'), ('appetizers', 'appetizers'), ('drinks', 'drinks'), ('treats', 'treats')], max_length=60),
        ),
    ]
