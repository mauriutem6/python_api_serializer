from rest_framework import serializers, viewsets, status
from webapp.models import usuario
from rest_framework.response import Response
from rest_framework.views import APIView

from django.db import models

class usuarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = usuario
        

        fields = '__all__'

    def to_representation(self, instance):
        usuario = super(usuarioSerializer, self).to_representation(instance)
        rut = instance.rut
        usuario['rut_ralacion'] = str(rut)
        return usuario

    

class IntanciausuarioView(APIView):
    def get(self, request, pk, format=None):
        query = usuario.objects.get(rut=pk)
        serializers = usuarioSerializer(query)
        return Response(serializers.data, status=status.HTTP_200_OK)



