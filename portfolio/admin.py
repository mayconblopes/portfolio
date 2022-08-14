from django.contrib import admin

from portfolio.models import Iam, About, Competence

admin.site.register(Iam)
admin.site.register(About)


@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'index_order', 'icon', 'name', 'description')
    list_editable = ('index_order', 'icon', 'name', 'description')
