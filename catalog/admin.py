from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

#admin.site.register(Book, BookAdmin)

# Define admin class
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

# Register class with associated model
#admin.site.register(Author, AuthorAdmin)
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass

#admin.site.register(BookInstance,BookInstanceAdmin)

admin.site.register(Genre)
admin.site.register(Language)

