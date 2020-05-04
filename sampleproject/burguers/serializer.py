from rest_framework import serializers
from .models import Hamburguesa, Ingrediente

#from django.contrib.auth.models import User
#from .models import Author, Book


# Serializers define the API representation.




class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente

        fields = ('id', 'nombre', 'descripcion')

class CustomIngredienteSerializer(IngredienteSerializer):



    ##ALTERAMOS REPRESTANCIÓN PARA QUE SIGA EL FORMATO DE LA API, E.G PATH
    def to_representation(self, instance):
        data = super(IngredienteSerializer, self).to_representation(instance)
        dir = "http://127.0.0.1:8000/ingrediente/{}".format(str(data['id']))
        return {'path': dir}



class HamburguesaSerializer(serializers.ModelSerializer):

    ingredientes = CustomIngredienteSerializer(many=True, required=False)

    class Meta:
        model = Hamburguesa
        fields = ('id', 'nombre', 'precio', 'descripcion', 'imagen', 'ingredientes')