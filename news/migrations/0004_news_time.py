# Generated by Django 2.2.5 on 2019-10-04 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20191004_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='time',
            field=models.CharField(default='00:00', max_length=12),
        ),
    ]