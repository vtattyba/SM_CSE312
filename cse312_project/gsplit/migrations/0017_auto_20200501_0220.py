# Generated by Django 3.0.4 on 2020-05-01 06:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gsplit', '0016_auto_20200501_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1c0c2283-8a88-4f4a-a75c-be28221e211b'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]