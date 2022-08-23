from django.contrib import admin

from blog.models import BlogPost, Author

admin.site.register(Author)


@admin.register(BlogPost)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'author', 'is_draft',)
    list_editable = ('is_draft',)
