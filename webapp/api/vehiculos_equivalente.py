from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import models
from rest_framework.permissions import IsAuthenticated
import json as xjson

from webapp.models import vehiculos_equivalente





class vehiculos_equivalenteSerializer(serializers.ModelSerializer):
    #usuario_track = persona_juridica_usuarioField(many=True, read_only=True)
    class Meta:
        model = vehiculos_equivalente
        fields = ['id','nombre']




class get_vehiculos_equivalente(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    serializer_class = vehiculos_equivalenteSerializer
    def get_queryset(self):
        queryset = vehiculos_equivalente.objects.filter(estado=1)
        return queryset
