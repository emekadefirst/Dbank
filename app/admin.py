from django.contrib import admin
from .models import CustomUser, UserGroupAssociation, UserPermissionAssociation

admin.site.register(CustomUser)
admin.site.register(UserGroupAssociation)
admin.site.register(UserPermissionAssociation)
