# Generated by Django 2.0.2 on 2018-02-21 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='photo',
            field=models.ImageField(default='photos/no_image.png', upload_to='photos/%Y/%m/%d'),
        ),
    ]
