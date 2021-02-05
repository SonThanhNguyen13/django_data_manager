from django.contrib import admin
from django import forms
from . import models
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ('username',)

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    add_form = UserCreationForm
    list_display = ("username", 'role')
    ordering = ("username",)

    fieldsets = (
        (None, {'fields': ('username', 'password', 'role', 'is_superuser', 'is_active')}),
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password', 'is_superuser', 'is_staff', 'role')}
            ),
        )

    list_filter = ["is_superuser", "role"]


class ShowRole(admin.ModelAdmin):
    list_display = ['role_id', 'role_name']
    list_filter = ('role_name',)
    

class ShowPermission(admin.ModelAdmin):
    list_display = ['permission_name', 'method', 'permission_url_name']
    list_filter = ('permission_name', 'method', 'permission_url_name')


class ShowRoleHasPermisson(admin.ModelAdmin):
    list_display = ["role", 'permission']
    list_filter = ["role", 'permission']


class ShowDatas(admin.ModelAdmin):
    list_per_page = 30
    list_display = ["data_id", 'name','data_category', "analyzed", "best_result", "best_analyzed_model", 'data_owner']
    list_filter = ["data_category", "analyzed", "best_analyzed_model", 'data_owner']


class ShowAiModels(admin.ModelAdmin):
    list_per_page = 30
    list_display = ['model_name', 'model_owner']
    list_filter = ['model_owner']


class ShowModelAndData(admin.ModelAdmin):
    list_per_page = 30
    list_display = ['data', 'data_category', 'data_owner', 'model', 'model_owner', 'added_by']

    def data_category(self, obj):
        return obj.data.data_category

    def data_owner(self, obj):
        return obj.data.data_owner

    def model_owner(self, obj):
        return obj.model.model_owner

    class Meta:
        model = models.ModelTrainData


admin.site.register(models.User, CustomUserAdmin)
admin.site.register(models.Role, ShowRole)
admin.site.register(models.Permission, ShowPermission)
admin.site.register(models.RoleHasPermisson, ShowRoleHasPermisson)
admin.site.register(models.DataCategory)
admin.site.register(models.Data, ShowDatas)
admin.site.register(models.AiModel, ShowAiModels)
admin.site.register(models.ModelTrainData, ShowModelAndData)
