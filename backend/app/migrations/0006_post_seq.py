# Generated by Django 2.1.3 on 2018-12-10 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20181210_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='seq',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
