from django.contrib import admin
from .models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
#    readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)} #prepopulated the slug fields with slugify format of title
    # sample technique to edit admin page display/settings
    list_filter = ("author", "rating",)
    list_display = ("title", "author",)
admin.site.register(Book, BookAdmin)