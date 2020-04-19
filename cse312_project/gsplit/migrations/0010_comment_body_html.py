# Generated by Django 3.0.5 on 2020-04-19 21:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gsplit', '0009_comment_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='body_html',
            field=models.TextField(default=django.utils.timezone.now, editable=False),
            preserve_default=False,
        ),
    ]