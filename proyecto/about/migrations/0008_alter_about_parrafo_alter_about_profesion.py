# Generated by Django 4.0.1 on 2022-01-27 05:38

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_remove_about_parrafo_1_remove_about_parrafo_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='parrafo',
            field=ckeditor.fields.RichTextField(verbose_name='Parrafos'),
        ),
        migrations.AlterField(
            model_name='about',
            name='profesion',
            field=models.CharField(max_length=50, verbose_name='Profesión'),
        ),
    ]