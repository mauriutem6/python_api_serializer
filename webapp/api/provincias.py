from rest_framework import serializers, viewsets, status
from webapp.models import Provincia
from webapp.api.comunas import ComunaTinySerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import(
    LimitOffsetPagination,
    PageNumberPagination
)

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 20



class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = '__all__'

    def to_representation(self, instance):
        objetoregion = super(ProvinciaSerializer, self).to_representation(instance)
        region = instance.region
        objetoregion['nombre_region'] = str(region)
        return objetoregion


class ProvinciaTinySerializer(serializers.ModelSerializer):
    """Tiny = Minúsculo, solo serializa id y nombre. Usado para el serializer RegionProvinciasSerializer"""
    class Meta:
        model = Provincia
        fields = ['id', 'nombre']
