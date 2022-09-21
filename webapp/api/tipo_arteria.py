from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import models
from rest_framework.permissions import IsAuthenticated

from webapp.models import tipo_arteria



import json as xjson

class tipo_arteriaSerializer(serializers.ModelSerializer):
    #usuario_track = persona_juridica_usuarioField(many=True, read_only=True)
    class Meta:
        model = tipo_arteria
        fields = ['id','nombre']




class get_tipo_arteria(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = tipo_arteriaSerializer
    def get_queryset(self):
        queryset = tipo_arteria.objects.filter(estado=1)
        return queryset
