from django.contrib import admin
from dang.models import Link, Category


class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'category', 'created_date')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}   



admin.site.register(Link, LinkAdmin)
admin.site.register(Category, CategoryAdmin)