# Generated by Django 3.1.5 on 2021-02-05 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_model_manager_app', '0011_data_note'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RoleHasPermisson',
            new_name='RoleHasPermission',
        ),
    ]
