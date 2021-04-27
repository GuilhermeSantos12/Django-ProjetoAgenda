from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Contato # Importando o Model Contato para trazer os contatos a paginas selecionadas
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
# --> Orderna os objectos pelo parametro selecionado, trazendo assim o contatos na pagina index ordenados. line(11)
# --> (-ID) traz os ultimos contatos adicionados por orden decrescente line (11)
# --> Paginator disponibiliza uma paginação na agenda exibindo apenas 10 contatos por pagina. lines(14 - 16)

def index(request): #Pagina index.html
    contatos = Contato.objects.order_by('-id').filter(
         mostrar=True
    )
    paginator = Paginator(contatos, 10)
    page_number = request.GET.get('p')
    contatos = paginator.get_page(page_number)
    return render(request, 'contatos/index.html',{
        'contatos': contatos
    })



# --> Verifica se o contato pode ser mostrado, isso garante que não haverá erros de constato já deletados ou excluidos pararecerem novamente. line(29-30)
def ver_contato(request, contato_id): #ver_contato.html
    contato = get_object_or_404(Contato, id=contato_id)


    if not contato.mostrar:
        raise  Http404()

    return render(request, 'contatos/ver_contato.html',{
        'contato': contato
    })


def busca(request):
    termo = request.GET.get('termo')

    if termo is None or not termo:
        messages.add_message(request, messages.ERROR,
                             'Campo termo não pode ficar vazio  ;)'
                             )
        return redirect('index')
    campos = Concat('nome',Value(''), 'sobrenome')

    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )
    paginator = Paginator(contatos, 10)
    page_number = request.GET.get('p')
    contatos = paginator.get_page(page_number)
    return render(request, 'contatos/busca.html',{
        'contatos': contatos
    })