# Generated by Django 3.0.5 on 2020-04-19 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsplit', '0005_auto_20200419_1357'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]