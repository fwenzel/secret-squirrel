from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import User

from .models import ClientSite


class ClientSiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain', 'match_priority')
    exclude = ('users',)
admin.site.register(ClientSite, ClientSiteAdmin)


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
