# Generated by Django 3.0.4 on 2020-05-01 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsplit', '0017_auto_20200501_0220'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]