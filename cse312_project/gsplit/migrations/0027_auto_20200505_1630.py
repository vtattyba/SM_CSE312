# Generated by Django 2.2.12 on 2020-05-05 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsplit', '0026_auto_20200505_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='liked',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
