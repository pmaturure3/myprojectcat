# Generated by Django 2.2.5 on 2019-10-26 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='email',
            field=models.TextField(default=''),
        ),
    ]
