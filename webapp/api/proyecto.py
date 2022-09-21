import datetime
from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import models
from rest_framework.permissions import IsAuthenticated
from webapp.models import proyecto, usuario, Comuna, Provincia, Region
import json as xjson



class proyectoSerializer(serializers.ModelSerializer):
    #usuario_track = persona_juridica_usuarioField(many=True, read_only=True)
    class Meta:
        model = proyecto
        fields = ['id','nombre','estado','usuario_creador','comuna_cod_comuna','fecha_creacion']
        #'total_terreno','superficie_util','superficie_edificada','tipo_tramite','rut_pertenece',

    def to_representation(self, instance):
        data = super(proyectoSerializer, self).to_representation(instance)
        #fecha_creacion = data['fecha_creacion']
        #otro = fecha_creacion.strftime('%Y-%m-%d %H:%M')
        #print(fecha_creacion)
        #print(datetime.datetime.strptime(str(fecha_creacion), '%Y-%m-%d').strftime('%d-%m-%Y'))
        #--------------------------------------------------------------------------
        #print(data['comuna_cod_comuna'])
        get_comuna = Comuna.objects.filter(id=data['comuna_cod_comuna'])
        for obj in get_comuna:
            provincia = obj.provincia
            provincia_id = provincia.id
            codigo_comuna = obj.codigo_comuna
            nombre_comuna = obj.nombre
            
            
        get_provincia = Provincia.objects.filter(id=provincia_id)
        for obj in get_provincia:
            region = obj.region
            region_id = region.id
            print(region_id)
        
        get_region = Region.objects.filter(id=region_id)
        for obj in get_region:
            nombre_region = obj.nombre
        #--------------------------------------------------------------------------

        data['region'] = nombre_region
        data['comuna'] = nombre_comuna
        

        data['usuario_creador'] = str(data['usuario_creador'])
        data.update()
        return data


class get_proyectoall(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    serializer_class = proyectoSerializer
    def get_queryset(self):
        rut_pertenece =self.request.query_params.get('rut','')
        estado =self.request.query_params.get('estado','')
        queryset = proyecto.objects.filter(rut_pertenece = rut_pertenece, estado ='2')
        return queryset


class get_proyectoe3(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    serializer_class = proyectoSerializer
    def get_queryset(self):
        rut_pertenece =self.request.query_params.get('rut','')
        queryset = proyecto.objects.filter(rut_pertenece = rut_pertenece, estado ='3')
        return queryset

