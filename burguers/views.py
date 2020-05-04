from django.shortcuts import render
from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
#from django.contrib.auth.models import User
#from .serializer import UserSerializer, AuthorSerializer, BookSerializer
#from .models import Author, Book
from rest_framework import filters
from .models import Hamburguesa, Ingrediente
from .serializer import HamburguesaSerializer, IngredienteSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser



# Create your views here.
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def hamburguesa_list(request):
    """
    List all code serie, or create a new serie.
    """

    if request.method == 'GET':
        hamburguesas = Hamburguesa.objects.all()
        serializer = HamburguesaSerializer(hamburguesas, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        try:
            data = JSONParser().parse(request)
        except:
            ##INPUT INVALIDO
            return HttpResponse(status=400)
        serializer = HamburguesaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            ##201 HAMBURGUESA CREADA
            return JSONResponse(serializer.data, status=201)

        ##INPUT INVALIDO
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def hamburguesa_detail(request, pk):
    """
    Retrieve, update or delete a serie.
    """

    ##manejor de error que pk sea un numero 400 ; ID INVALIDO
    for char in pk:
        if char not in ["1","2","3","4","5","6","7","8","9","0"]:
            return HttpResponse(status=400)


    try:
        hamburguesa = Hamburguesa.objects.get(pk=pk)
    except Hamburguesa.DoesNotExist:
        #404 : HAMBURGUESA INEXISTENTE
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = HamburguesaSerializer(hamburguesa)
        return JSONResponse(serializer.data)

    elif request.method == 'DELETE':
        hamburguesa.delete()
        #200: HAMBURGUESA ELIMINDA
        return HttpResponse(status=200)

    elif request.method == 'PATCH':
        try:
            data = JSONParser().parse(request)
        except:
            #PARAMETROS INVALIDADOS
            return HttpResponse(status=400)

        serializer = HamburguesaSerializer(hamburguesa, data=data)
        if serializer.is_valid():
            serializer.save()
            ##200: OPERACIÓN EXITOSA
            return JSONResponse(serializer.data, status=200)
        #PARAMETROS INVALIDOS
        return JSONResponse(serializer.errors, status=400)




@csrf_exempt
def ingrediente_list(request):
    """
    List all code serie, or create a new serie.
    """
   # actions =  ['GET', 'POST']

    ##SINO ES UNA ACCIÓN VALIDA DADA POR EL PROTOCOLO, LANZO ERROR
    #if request.method not in actions:
     #   return HttpResponse(status=404)

    if request.method == 'GET':
        ingredientes = Ingrediente.objects.all()
        serializer = IngredienteSerializer(ingredientes, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        try:
            data = JSONParser().parse(request)
        except:
            ##INPUT INVALIDO
            return HttpResponse(status=400)
        serializer = IngredienteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            ##201 HAMBURGUESA CREADA
            return JSONResponse(serializer.data, status=201)

        ##INPUT INVALIDO
        return JSONResponse(serializer.errors, status=400)



@csrf_exempt
def ingrediente_detail(request, pk):
    """
    Retrieve, update or delete a serie.
    """

    ##manejor de error que pk sea un numero
    for char in pk:
        if char not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            return HttpResponse(status=400)

    try:
        ingrediente = Ingrediente.objects.get(pk=pk)
    except Ingrediente.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = IngredienteSerializer(ingrediente)
        return JSONResponse(serializer.data)

    elif request.method == 'DELETE':

        ##409 	 Ingrediente no se puede borrar, se encuentra presente en una hamburguesa

        for burga in Hamburguesa.objects.all():

            if ingrediente in burga.ingredientes.all():
                #print("ESTA PRESENTE")
                return HttpResponse(status=409)

        ingrediente.delete()
        #print("boraradno")
        return HttpResponse(status=200)


@csrf_exempt
def ingrediente_hamburguesa(request, pk_hamb, pk_ingred):
    ##manejor de error que pk sea un numero
    for char in pk_hamb:
        if char not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            return HttpResponse(status=400)

    ##manejor de error que pk sea un numero
    for char in pk_ingred:
        if char not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            return HttpResponse(status=400)


    ##OBTENIENDO HAMBURGUESA...
    try:
        hamburguesa = Hamburguesa.objects.get(pk=pk_hamb)
    except Hamburguesa.DoesNotExist:
        return HttpResponse(status=404)


    ##OBTENIENDO INGREDIENTE...
    try:
        ingrediente = Ingrediente.objects.get(pk=pk_ingred)
    except Ingrediente.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'PUT':
        hamburguesa.ingredientes.add(ingrediente)
        ##Ingrediente agregado: 201
        return HttpResponse(status=201)


    elif request.method == 'DELETE':
        if ingrediente in hamburguesa.ingredientes.all():
            hamburguesa.ingredientes.remove(ingrediente)
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=404)
