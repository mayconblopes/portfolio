from django.contrib import admin
from portfolio.models import Iam, About, Competence, Experience, Award, Papper, PortfolioItem

admin.site.register(Iam)
admin.site.register(About)

@admin.register(Experience)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'index_order')
    list_editable = ('index_order',)


@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'index_order', 'icon', 'name', 'description')
    list_editable = ('index_order', 'icon', 'name', 'description')


@admin.register(Papper)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('title', 'index_order')
    list_editable = ('index_order',)


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('who', 'description', 'index_order')
    list_editable = ('index_order',)


@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_owner', 'index_order')
    list_editable = ('index_order',)
