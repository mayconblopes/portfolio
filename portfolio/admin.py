from django.contrib import admin

from portfolio.models import Iam, About, Competence, Experience

admin.site.register(Iam)
admin.site.register(About)
admin.site.register(Experience)


@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'index_order', 'icon', 'name', 'description')
    list_editable = ('index_order', 'icon', 'name', 'description')
