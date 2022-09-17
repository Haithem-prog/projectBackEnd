from django.contrib import admin

from custom_user.models import CustomUser
from .models import Book, Author, Genre, Items

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'pages', 'genre', 'author','total_sales', 'published']


class ItemsAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'qty', 'inCart', 'isBought']


class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id',  'name']
class UserAdmin(admin.ModelAdmin):
    list_display = ['id',  'name', 'phone']


admin.site.register(Book, BookAdmin)
admin.site.register(Items, ItemsAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)

admin.site.register(CustomUser, UserAdmin)

# list_filter = ('',)
# raw_id_fields = ('',)
# readonly_fields = ('',)
# search_fields = ('',)
# date_hierarchy = ''
# ordering = ('',)
