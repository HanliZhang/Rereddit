# Generated by Django 2.1.1 on 2018-10-25 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20181025_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followtag',
            name='tag',
            field=models.ManyToManyField(related_name='tag_set', to='app.Tag'),
        ),
    ]
