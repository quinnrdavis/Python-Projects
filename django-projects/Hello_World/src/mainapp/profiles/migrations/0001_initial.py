# Generated by Django 4.1 on 2022-08-05 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, default='', max_length=60)),
                ('lname', models.CharField(blank=True, default='', max_length=60)),
                ('email', models.CharField(blank=True, default='', max_length=60)),
                ('username', models.CharField(blank=True, default='', max_length=60)),
            ],
        ),
    ]
