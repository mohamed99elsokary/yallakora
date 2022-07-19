from django.contrib import admin
from .models import Social

class SocialAdmin(admin.ModelAdmin):
    list_display = ('facebook', 'instagram', 'youtube')
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Social, SocialAdmin)
