# Generated by Django 2.1.1 on 2018-10-17 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20181017_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('FEMALE', 'Female'), ('MALE', 'Male')], max_length=20),
        ),
    ]
