from django.shortcuts import render, get_object_or_404


from django.http import HttpResponse
from django.template import loader
from core.models import Produto

# Create your views here.


def index(request):
    produtos = Produto.objects.all()
    context = {
        'curso': 'Programação web com Django Framework',
        'outraChave': 'Django é massa',
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    #prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)

    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)

def error404(request, exception):
    template = ren
    return render(request, '404.html')