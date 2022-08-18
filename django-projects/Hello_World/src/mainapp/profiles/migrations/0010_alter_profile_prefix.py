# Generated by Django 4.1 on 2022-08-18 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_alter_profile_prefix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='prefix',
            field=models.CharField(blank=True, choices=[('Dr.', 'Dr.'), ('Mrs.', 'Mrs.'), ('Mr.', 'Mr.'), ('Ms.', 'Ms.')], max_length=60, null=True),
        ),
    ]
