# Generated by Django 3.1.2 on 2020-10-20 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trytest', '0002_auto_20201019_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='PhoneNumber',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='StudentNumber',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]