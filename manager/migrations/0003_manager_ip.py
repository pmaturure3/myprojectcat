# Generated by Django 2.2.5 on 2019-11-01 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_manager_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='ip',
            field=models.TextField(default=''),
        ),
    ]
