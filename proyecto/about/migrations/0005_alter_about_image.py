# Generated by Django 4.0.1 on 2022-01-24 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_alter_about_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(upload_to='Project', verbose_name='Foto de Perfil'),
        ),
    ]
