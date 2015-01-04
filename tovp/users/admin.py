from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import User
from .forms import UserCreationForm, UserChangeForm


class UserProfileAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'display_name', 'is_admin')
    list_filter = ('is_admin',)
    # fieldsets = (
    #     (None, {'fields': ('username', 'password')}),
    #     ('Permissions', {'fields': ('is_admin',)}),
    # )
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'password1', 'password2')}),
        (_('Personal info'), {'fields': ['display_name', 'about']}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'password1', 'password2')}),
        (_('Personal info'), {'fields': ['display_name', 'about']}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('username', 'display_name', 'password1', 'password2')}
    #     ),
    # )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(User, UserProfileAdmin)
