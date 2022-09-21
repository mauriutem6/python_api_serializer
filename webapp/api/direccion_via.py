from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import models
from rest_framework.permissions import IsAuthenticated

from webapp.models import direccion_via



import json as xjson

class direccion_viaSerializer(serializers.ModelSerializer):
    #usuario_track = persona_juridica_usuarioField(many=True, read_only=True)
    class Meta:
        model = direccion_via
        fields = ['id','nombre']




class get_direccion_via(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = direccion_viaSerializer
    def get_queryset(self):
        queryset = direccion_via.objects.all()
        return queryset
