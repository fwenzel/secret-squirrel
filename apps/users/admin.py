from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import User

from sso.models import ClientSite


class UserSitesInline(admin.StackedInline):
    """Show authorized ClientSites inline with user admin."""
    model = ClientSite.users.through
    verbose_name = 'Site'
    verbose_name_plural = 'Associated Sites'

class UserAdmin(DjangoUserAdmin):
    """Subclass for Django's built-in user admin, to include inline(s)"""
    inlines = [UserSitesInline]
admin.site.unregister(User) # remove built-in admin
admin.site.register(User, UserAdmin)
