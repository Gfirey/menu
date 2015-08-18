from django.contrib import admin
from custom_menu import models


class NodeModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}


admin.site.register(models.NodeModel, NodeModelAdmin)
admin.site.register(models.Menu)
