# Generated by Django 3.1.5 on 2021-02-19 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_model_manager_app', '0013_auto_20210208_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeltraindata',
            name='result',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
