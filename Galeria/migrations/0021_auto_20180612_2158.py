# Generated by Django 2.0.6 on 2018-06-12 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Galeria', '0020_auto_20180612_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='titulo',
            field=models.CharField(default='2018-06-12 21:58:32.657692', max_length=40),
        ),
        migrations.AlterField(
            model_name='multimedia',
            name='titulo',
            field=models.CharField(default='image2018-06-12 21:58:32.658542', max_length=80),
        ),
    ]
