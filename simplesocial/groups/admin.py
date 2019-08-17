from django.contrib import admin
from . import models

# Register your models here.

#inline class using will utlz
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
