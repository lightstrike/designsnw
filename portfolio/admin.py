from django.contrib import admin

from .models import Portfolio, PortfolioImage


class SortableAdmin(admin.StackedInline):
    sortable_field_name = "order"
    extra = 0


class PortfolioImageInline(SortableAdmin):
    model = PortfolioImage


class PortfolioAdmin(admin.ModelAdmin):
    model = Portfolio
    inlines = (PortfolioImageInline, )


admin.site.register(Portfolio, PortfolioAdmin)
