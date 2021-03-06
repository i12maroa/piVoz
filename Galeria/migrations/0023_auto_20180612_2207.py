# Generated by Django 2.0.6 on 2018-06-12 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Galeria', '0022_auto_20180612_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='titulo',
            field=models.CharField(default='2018-06-12 22:07:50.811533', max_length=40),
        ),
        migrations.AlterField(
            model_name='multimedia',
            name='keyword',
            field=models.ManyToManyField(help_text='Selecciona las Personas que aparezcan en la foto', to='Galeria.Keyword'),
        ),
        migrations.AlterField(
            model_name='multimedia',
            name='titulo',
            field=models.CharField(default='image2018-06-12 22:07:50.812380', max_length=80),
        ),
    ]
