from django.contrib import admin
from phone.models import PhoneBrand, PhoneModel, Phone
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.admin import ModelAdmin


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


@admin.register(PhoneBrand)
class PhoneBrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'nationality')
    list_filter = ('name', 'nationality')
    search_fields = ('name', 'nationality')


@admin.register(PhoneModel)
class PhoneModelAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand')
    list_filter = ('brand',)


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = (
        'phone_name', 'color', 'screen_size', 'price',
        'is_available', 'manufacturing_country'
    )
    list_filter = (
        'phone_name__brand', 'color', 'price', 'is_available', 'manufacturing_country'
    )
