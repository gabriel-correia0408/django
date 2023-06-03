from django.shortcuts import render

# Create your views here.


def index(request):
    print(dir(request.user))
    print(f'Metodo:{request.method}')
    print(f"User: {request.user}")
    print(f"GETHOST: {request.get_host}")
    print(f"ISSECURE: {request.is_secure}")

    if str(request.user) == 'AnonymousUser':
        teste = 'Usuario nao logado'
    else:
        teste = 'Usuario  logado'

    context = {
        'curso': 'Programação web com Django Framework',
        'outraChave': 'Django é massa',
        'logado': teste
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')