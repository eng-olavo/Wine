from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def adega(request):
    return render(request,'adega.html')


def adicionarVinho(request):
    return render(request,'adicionarVinho.html')

