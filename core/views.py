from django.shortcuts import render
from core.models import Vinho

def index(request):
    return render(request,'index.html')


def adega(request):
    vinho = Vinho.objects.all()
    dados = {'vinhos': vinho}
    print(vinho)
    return render(request, 'adega.html', dados)


def adicionarVinho(request):
    return render(request,'adicionarVinho.html')

