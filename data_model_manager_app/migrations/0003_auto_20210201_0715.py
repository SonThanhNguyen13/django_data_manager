# Generated by Django 3.1.5 on 2021-02-01 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_model_manager_app', '0002_data_data_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modeltraindata',
            old_name='data_id',
            new_name='data_name',
        ),
        migrations.RenameField(
            model_name='modeltraindata',
            old_name='model_id',
            new_name='model_name',
        ),
    ]