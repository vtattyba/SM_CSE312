# Generated by Django 3.0.4 on 2020-05-06 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gsplit', '0004_auto_20200505_2322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follows',
            name='followee',
        ),
        migrations.RemoveField(
            model_name='follows',
            name='follower',
        ),
    ]
