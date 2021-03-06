# Generated by Django 2.0.6 on 2018-06-11 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Galeria', '0008_auto_20180611_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='image_height',
            field=models.PositiveSmallIntegerField(default=400),
        ),
        migrations.AddField(
            model_name='album',
            name='image_width',
            field=models.PositiveSmallIntegerField(default=400),
        ),
        migrations.AlterField(
            model_name='album',
            name='thumbnail',
            field=models.ImageField(height_field=models.PositiveSmallIntegerField(default=400), upload_to='thumbs', width_field=models.PositiveSmallIntegerField(default=400)),
        ),
        migrations.AlterField(
            model_name='album',
            name='titulo',
            field=models.CharField(default='2018-06-11 18:44:41.526872', max_length=40),
        ),
        migrations.AlterField(
            model_name='multimedia',
            name='titulo',
            field=models.CharField(default='image2018-06-11 18:44:41.527705', max_length=80),
        ),
    ]
