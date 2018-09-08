from django.contrib import admin

from . import models


class GroupMemberInline(admin.TabularInline):
    model = models.User



admin.site.register(models.User)
