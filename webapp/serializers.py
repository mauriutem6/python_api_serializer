#-------------------------------django-----------------------------------------------------
from rest_framework import serializers
#-------------------------------local------------------------------------------------------

from . models import empresa
from . models import usuario, persona_juridica, persona_juridica_usuario

class empresaSerializer(serializers.ModelSerializer):

	class Meta:
		model = empresa
		#fields=('firstname', 'lastname')
		fields='__all__'



class usuarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = usuario
		fields='__all__'


class persona_juridicaSerializer(serializers.ModelSerializer):
	class Meta:
		model = persona_juridica
		fields='__all__'

class persona_juridica_usuarioSerializer(serializers.ModelSerializer):
	persona_juridica_data = persona_juridicaSerializer(read_only=True, many=True)
	class Meta:
		model = persona_juridica_usuario
		fields='__all__'	

