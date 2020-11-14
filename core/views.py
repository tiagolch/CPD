from django.shortcuts import render, redirect, get_object_or_404
from .forms import *


def index(request):
    return render(request, 'index.html')


def cadastro_tonners(request):
    form = TonnersForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listagem_tonners')
    return render(request, "cadastro_tonners.html", {'form': form})


def atualizacao_tonners(request, id):
    tonners = get_object_or_404(Tonners, pk=id)
    form = TonnersForm(request.POST or None, instance=tonners)
    if form.is_valid():
        form.save()
        return redirect('listagem_tonners')
    return render(request, 'cadastro_tonners.html', {'form': form})


def delete_tonners(request, id):
    tonners = get_object_or_404(Tonners, pk=id)
    if request.method == 'POST':
        tonners.delete()
        return redirect('listagem_tonners')
    return render(request, 'delete_tonners_confirm.html', {'tonners': tonners})


def listagem_tonners(request):
    list = Tonners.objects.all()
    return render(request, "listagem_tonners.html", {'lista': list})

