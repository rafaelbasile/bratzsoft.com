# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.forms import UserChangeForm, UserCreationForm
# from .models import User
# from django import forms
#
#
# class UserChangeForm(UserChangeForm):
#     class Meta(UserChangeForm.Meta):
#         model = User
#
#
# class UserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = User
#
#     def clean_username(self):
#         username = self.cleaned_data['username']
#         try:
#             User.objects.get(username=username)
#         except User.DoesNotExist:
#             return username
#         raise forms.ValidationError(self.error_messages['duplicate_username'])
#
#
# class UserAdmin(UserAdmin):
#     form = UserChangeForm
#     add_form = UserCreationForm
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('extra_field1', 'extra_field2',)}),
#     )
#
# admin.site.register(User, UserAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ()
    #list_display = ('username','sid','client')
    #search_fields = ['username','sid']
    #list_filter = ('sid','active')







#Admin Registrations

admin.site.register(User, UserAdmin)
