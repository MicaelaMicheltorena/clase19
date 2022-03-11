from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import random

def inicio(request):
  return HttpResponse("Hola, soy la nueva pagina")


def otra_vista(request):
  return HttpResponse("<h1> Este es un titulo en h1</h1>")  
  

def numero_random(request):
  numero = random.randrange(15, 180)
  texto = f"<h1> Este es tu numero random: {numero}</h1>"
  return HttpResponse(texto)


def numero_del_usuario(request, numero):
  texto = f"<h1> Este es tu numero: {numero}</h1>"
  return HttpResponse(texto)

