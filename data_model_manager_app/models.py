from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.


class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=512)
    
    def __str__(self):
        return self.role_name


class AccountUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, role_id=None, **extra_fields):
        user = self.create_user(
            username=username,
            password=password,
            role_id=role_id,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(PermissionsMixin, AbstractBaseUser):
    username = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=512)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, default=1)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    token = models.CharField(max_length=512, blank=True, default=None, null=True)
    objects = AccountUserManager()
    REQUIRED_FIELD = ['role_id', ]
    USERNAME_FIELD = 'username'
    
    def __str__(self):
        return self.username


class Permission(models.Model):
    permission_id = models.AutoField(primary_key=True)
    permission_name = models.CharField(max_length=512)
    method = models.CharField(
        max_length=20,
        choices=(
            ('GET', 'GET'),
            ('POST', 'POST'),
            ('PUT', 'PUT'),
            ('DELETE', 'DELETE')
        )
    )
    permission_url_name = models.CharField(max_length=512)

    def __str__(self):
        return self.permission_name


class RoleHasPermisson(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)


class DataCategory(models.Model):
    data_category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class AiModel(models.Model):
    model_id = models.AutoField(primary_key=True)
    model_name = models.CharField(max_length=512)
    model_owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.model_name

# mai fix :D
class Data(models.Model):
    data_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=512)
    data_category = models.ForeignKey(DataCategory, on_delete=models.CASCADE)
    size_on_disk = models.FloatField()
    directory_of_data = models.CharField(max_length=512, blank=True, null=True)
    number_of_images = models.PositiveIntegerField()
    number_of_classes = models.PositiveIntegerField(null=True, blank=True)
    brisque = models.FloatField(null=True, blank=True)
    brightness = models.FloatField(null=True, blank=True)
    sharpness = models.FloatField(null=True, blank=True)
    iqa_3 = models.FloatField(null=True, blank=True)
    iqa_4 = models.FloatField(null=True, blank=True)
    mean_width = models.FloatField(null=True, blank=True)
    mean_height = models.FloatField(null=True, blank=True)
    shape_2 = models.FloatField(null=True, blank=True)
    shape_3 = models.FloatField(null=True, blank=True)
    shape_4 = models.FloatField(null=True, blank=True)
    analyzed = models.BooleanField(default=False)
    best_result = models.CharField(max_length=512, null=True, blank=True)
    best_analyzed_model = models.ForeignKey(AiModel, on_delete=models.SET_NULL, null=True, blank=True)
    data_avatar = models.ImageField(upload_to="data/data_avatar", default=None, null=True, blank=True)
    note = models.CharField(null=True, blank=True, max_length=1024)
    data_owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class ModelTrainData(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.ForeignKey(Data, on_delete=models.CASCADE)
    model = models.ForeignKey(AiModel, on_delete=models.CASCADE)
    added_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    result = models.FloatField(default=0.0)
