# Generated by Django 3.1.5 on 2021-02-02 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_model_manager_app', '0008_auto_20210202_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='best_result',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
