from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import models
from rest_framework.permissions import IsAuthenticated

from webapp.models import tipo_area



import json as xjson

class tipo_areaSerializer(serializers.ModelSerializer):
    #usuario_track = persona_juridica_usuarioField(many=True, read_only=True)
    class Meta:
        model = tipo_area
        fields = ['id','nombre']




class get_tipo_area(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = tipo_areaSerializer
    def get_queryset(self):
        queryset = tipo_area.objects.filter(estado=1)
        return queryset
