# Generated by Django 2.1.1 on 2018-10-17 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20181017_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(default='', max_length=20),
        ),
    ]
