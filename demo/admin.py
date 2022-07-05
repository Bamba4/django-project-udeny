from django.contrib import admin

from demo.models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # fields = ['title', 'description']
    list_display = ['title', 'price', 'description']
    list_filter = ['published']
    search_fields = ['title', 'description']