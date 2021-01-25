def reprovar_comentarios(modeladmin, request, queryset):
    queryset.update(aprovado=False)


def aprovar_comentarios(modeladmin, request, queryset):
    queryset.update(aprovado=True)


reprovar_comentarios.short_description = 'Reprovar comentarios'

aprovar_comentarios.short_description = 'Aprovar comentarios'
