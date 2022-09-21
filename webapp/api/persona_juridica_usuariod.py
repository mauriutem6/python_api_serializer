from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import models
from rest_framework.permissions import IsAuthenticated

from webapp.models import usuario, persona_juridica_usuario, persona_juridica





class persona_juridicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = persona_juridica
        fields = ['rut', 'nombre']



class persona_juridica_usuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = persona_juridica_usuario
        fields = ['usuario_rut','persona_juridic_id']




class usuarioSerializer(serializers.ModelSerializer):
    usuario_rut = persona_juridica_usuarioSerializer(many=True, read_only=True)

    class Meta:
        model = usuario
        fields = ['rut', 'ape_pat', 'usuario_rut']


class persona_juridica_usuarioSearchd(viewsets.ModelViewSet):
    serializer_class = usuarioSerializer
    def get_queryset(self):
        #queryset = usuario.objects.all()
        print("******************************************hola")
        queryset = usuario.objects.filter(rut = '14905763')
        print(queryset)
        print("******************************************hola2")
        """
        rut =self.request.query_params.get('rut','')
        if len(rut):
            queryset = queryset.filter(nombre__icontains=rut)
        """ 
        
        return queryset
