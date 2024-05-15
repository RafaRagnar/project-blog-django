from django.contrib import admin
from django.http import HttpRequest
from site_setup.models import MenuLink, SiteSetup


@admin.register(MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
    list_display: tuple = ('id', 'text', 'url_or_path',)
    list_display_links: tuple = ('id', 'text', 'url_or_path',)
    search_fields: tuple = ('id', 'text', 'url_or_path',)


@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display: tuple = ('title', 'description')

    def has_add_permission(self, request: HttpRequest) -> bool:
        return not SiteSetup.objects.exists()
