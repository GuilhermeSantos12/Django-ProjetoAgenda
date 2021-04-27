from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email',
                    'data_criacao', 'categoria', 'mostrar') # Mostra quais atributos seram apresnetados no display da pg amin
    list_display_links = ('id', 'nome', 'sobrenome') # Disponibiliza a edição nos atrbiutos dentro da tupla apenas clicnado
    #list_filter = ('nome', 'sobrenome')# Disponibiliza um Filtro com os atributos selecionados na tupla
    list_per_page = 10 #Será exibido apenas 10 elementos por pagina
    search_fields = ('nome', 'sobrenome', 'telefone', 'email')# Campo de pesquisa
    list_editable = ('telefone', 'mostrar')
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)