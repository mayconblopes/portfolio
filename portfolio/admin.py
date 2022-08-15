from django.contrib import admin

from portfolio.models import Iam, About, Competence, Experience, Award

admin.site.register(Iam)
admin.site.register(About)
admin.site.register(Experience)


@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'index_order', 'icon', 'name', 'description')
    list_editable = ('index_order', 'icon', 'name', 'description')


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('who', 'description', 'index_order')
    list_editable = ('index_order',)
