from django.contrib import admin
from blog.models import Tag, Category


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display: tuple = ('id', 'name', 'slug')
    list_display_links: tuple = ('name',)
    search_fields: tuple = ('id', 'name', 'slug')
    list_per_page: int = 10
    ordering: tuple = ('-id',)
    prepopulated_fields: dict = {
        "slug": ('name',),
    }


@admin.register(Category)
class CagetoryAdmin(admin.ModelAdmin):
    list_display: tuple = ('id', 'name', 'slug')
    list_display_links: tuple = ('name',)
    search_fields: tuple = ('id', 'name', 'slug')
    list_per_page: int = 10
    ordering: tuple = ('-id',)
    prepopulated_fields: dict = {
        "slug": ('name',),
    }
