# Generated by Django 3.1.5 on 2021-01-29 04:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=25, unique=True)),
                ('password', models.CharField(max_length=512)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('token', models.CharField(blank=True, default=None, max_length=512, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AiModel',
            fields=[
                ('model_id', models.AutoField(primary_key=True, serialize=False)),
                ('model_name', models.CharField(max_length=512)),
                ('model_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('data_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=512)),
                ('size_on_disk', models.PositiveIntegerField()),
                ('directory_of_data', models.CharField(blank=True, max_length=512, null=True)),
                ('number_of_images', models.PositiveIntegerField()),
                ('number_of_classes', models.PositiveIntegerField(blank=True, null=True)),
                ('iqa_0', models.PositiveIntegerField(blank=True, null=True)),
                ('iqa_1', models.PositiveIntegerField(blank=True, null=True)),
                ('iqa_2', models.PositiveIntegerField(blank=True, null=True)),
                ('iqa_3', models.PositiveIntegerField(blank=True, null=True)),
                ('iqa_4', models.PositiveIntegerField(blank=True, null=True)),
                ('shape_0', models.PositiveIntegerField(blank=True, null=True)),
                ('shape_1', models.PositiveIntegerField(blank=True, null=True)),
                ('shape_2', models.PositiveIntegerField(blank=True, null=True)),
                ('shape_3', models.PositiveIntegerField(blank=True, null=True)),
                ('shape_4', models.PositiveIntegerField(blank=True, null=True)),
                ('analyzed', models.BooleanField(default=False)),
                ('best_result', models.FloatField(blank=True, null=True)),
                ('data_avatar', models.ImageField(blank=True, default=None, null=True, upload_to='data/data_avatar')),
                ('best_analyzed_model', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='data_model_manager_app.aimodel')),
            ],
        ),
        migrations.CreateModel(
            name='DataCategory',
            fields=[
                ('data_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('permission_id', models.AutoField(primary_key=True, serialize=False)),
                ('permission_name', models.CharField(max_length=512)),
                ('method', models.CharField(choices=[('GET', 'GET'), ('POST', 'POST'), ('PUT', 'PUT'), ('DELETE', 'DELETE')], max_length=20)),
                ('permission_url_name', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='RoleHasPermisson',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_model_manager_app.permission')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_model_manager_app.role')),
            ],
        ),
        migrations.CreateModel(
            name='ModelTrainData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_model_manager_app.data')),
                ('model_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_model_manager_app.aimodel')),
            ],
        ),
        migrations.AddField(
            model_name='data',
            name='data_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_model_manager_app.datacategory'),
        ),
        migrations.AddField(
            model_name='user',
            name='role_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='data_model_manager_app.role'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
