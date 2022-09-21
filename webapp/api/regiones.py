
from rest_framework import serializers, viewsets, status
from rest_framework.decorators import action


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import(
    LimitOffsetPagination,
    PageNumberPagination
)


from webapp.api.provincias import ProvinciaTinySerializer
from webapp.api.comunas import ComunaTinySerializer
from webapp.models import Region, Comuna


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 20

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class RegionProvinciasSerializer(serializers.ModelSerializer):
    """Serializa las regiones con sus provincias"""
    provincias_region = ProvinciaTinySerializer(read_only=True, many=True)

    class Meta:
        model = Region
        fields = ['id', 'nombre', 'provincias_region']



class RegionProvinciasView(viewsets.ModelViewSet):
    """Devuelve las regiones y sus provincias (en ambos casos solamente nombre e id)"""
    queryset = Region.objects.all()
    serializer_class = RegionProvinciasSerializer

    @action(detail=True, methods=['get'])
    def comunas(self, request, pk=None):
        __comunas = Comuna.objects.filter(provincia__region_id=pk)
        serializer = ComunaTinySerializer(instance=__comunas, many=True)
        return Response(serializer.data)


class RegionView(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
