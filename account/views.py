from django.shortcuts import render, redirect
from .models import Transacao
from .form import TransacaoForm

def home(request):
    data = {}

    data['transactions'] = Transacao.objects.all()

    return render(request, 'account/home.html', data)

def create(request):
    form = TransacaoForm(request.POST or None) # chegando aqui, sera procurado se tem algum dado preenchido

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'account/create.html', {'form': form})

def update(request, pk):
    transaction = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transaction) # comecando um form com o objeto do banco

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'account/create.html', {'form': form, 'transaction': transaction})

def delete(request, pk):
    transaction = Transacao.objects.get(pk=pk)
    transaction.delete()

    return redirect('home')