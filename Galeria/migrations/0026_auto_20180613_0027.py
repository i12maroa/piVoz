# Generated by Django 2.0.6 on 2018-06-12 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Galeria', '0025_auto_20180612_2214'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'verbose_name_plural': 'Álbumes'},
        ),
        migrations.AlterField(
            model_name='album',
            name='titulo',
            field=models.CharField(default='2018-06-13 00:27:51.159863', max_length=40),
        ),
        migrations.AlterField(
            model_name='multimedia',
            name='titulo',
            field=models.CharField(default='image2018-06-13 00:27:51.163054', max_length=80),
        ),
    ]