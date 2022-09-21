from rest_framework import serializers, viewsets, status
from webapp.models import Comuna
from rest_framework.response import Response
from rest_framework.views import APIView

class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = '__all__'

    def to_representation(self, instance):
        objetoregionprovincia = super(ComunaSerializer, self).to_representation(instance)
        provincia = instance.provincia
        objetoregionprovincia['nombre_provincia'] = str(provincia)
        return objetoregionprovincia



class ComunaView(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer



class ComunaSearch(viewsets.ModelViewSet):    
    serializer_class = ComunaSerializer
    #pagination_class = LargeResultsSetPagination
    def get_queryset(self):
        queryset = Comuna.objects.all()
        nombre =self.request.query_params.get('nombre','')
        if len(nombre):
            queryset = queryset.filter(nombre__icontains=nombre)
        return queryset

class IntanciaComunaDetailView(APIView):
    def get(self, request, pk, format=None):
        query = Comuna.objects.get(codigo_comuna=pk)
        serializers = ComunaSerializer(query)
        return Response(serializers.data, status=status.HTTP_200_OK)

def get(self, request, pk, format=None):
        query = Comuna.objects.get(codigo_comuna=pk)
        serializers = ComunaSerializer(query)
        return Response(serializers.data, status=status.HTTP_200_OK)


class ComunaTinySerializer(serializers.ModelSerializer):
    """Tiny = Minúsculo, solo serializa id y nombre. Usado para el serializer ProvinciaComunasSerializer"""
    class Meta:
        model = Comuna
        fields = ['id', 'nombre']
