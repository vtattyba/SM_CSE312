# Generated by Django 3.0.4 on 2020-05-06 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsplit', '0013_auto_20200506_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='like_f',
        ),
        migrations.AddField(
            model_name='post',
            name='liked',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]