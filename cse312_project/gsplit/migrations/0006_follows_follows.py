# Generated by Django 3.0.4 on 2020-05-06 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsplit', '0005_auto_20200506_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='follows',
            name='follows',
            field=models.ManyToManyField(to='gsplit.UserProfile'),
        ),
    ]
