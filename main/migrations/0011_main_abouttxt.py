# Generated by Django 2.2.5 on 2019-10-12 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20191011_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='abouttxt',
            field=models.TextField(default=''),
        ),
    ]
