from django.contrib import admin

from library.models import books

# Register your models here.
@admin.register(books)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id','name','subject','author','publish']