from django.shortcuts import render

from .models import Pergunta
# Create your views here.

def index(request):
    todas = Pergunta.objects.all()
    return render(request, 'index.html', {
        "perguntas": todas
    })

def responder(request, num_pergunta):
    pergunta = Pergunta.objects.get(pk=num_pergunta)
    return render(request, 'responder.html', {
        "pergunta": pergunta
    })
