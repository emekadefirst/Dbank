from django.conf import settings
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    fullname = models.CharField(max_length=255, default=True)
    balance = models.IntegerField(default=1000)

    # Your additional fields go here

    # ...

    def add_group(self, group):
        UserGroupAssociation.objects.get_or_create(user=self, group=group)

    def remove_group(self, group):
        UserGroupAssociation.objects.filter(user=self, group=group).delete()

    def add_permission(self, permission):
        UserPermissionAssociation.objects.get_or_create(
            user=self, permission=permission)

    def remove_permission(self, permission):
        UserPermissionAssociation.objects.filter(
            user=self, permission=permission).delete()


class UserGroupAssociation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class UserPermissionAssociation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
