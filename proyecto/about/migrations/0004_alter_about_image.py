# Generated by Django 4.0.1 on 2022-01-27 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_alter_about_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(upload_to='Project', verbose_name='Foto de Perfil'),
        ),
    ]
