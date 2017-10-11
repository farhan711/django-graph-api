from django.contrib import admin
from graph.models import Graph, GraphData


class GraphDataInline(admin.StackedInline):
    model = GraphData
    extra = 1
    verbose_name_plural = 'Graph Data'


class GraphAdmin(admin.ModelAdmin):
    model = Graph
    list_display = ('name', 'description', 'color_code', 'date_created')
    search_fields = ['name']
    readonly_fields = ['date_created', 'date_modified']
    inlines = (GraphDataInline,)


admin.site.register(Graph, GraphAdmin)
