<<<<<<< HEAD
# Generated by Django 4.0.1 on 2022-01-23 21:53
=======
# Generated by Django 4.0.1 on 2022-01-24 03:51
>>>>>>> 7aa53a6dd013dc37f354cf930508aa4e74b902c0

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_remove_project_link_facebook_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('-created',), 'verbose_name': 'Proyecto', 'verbose_name_plural': 'Proyectos'},
        ),
        migrations.RenameField(
            model_name='project',
            old_name='crated',
            new_name='created',
        ),
    ]