from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import models
from rest_framework.permissions import IsAuthenticated

from webapp.models import usuario, persona_juridica_usuario, persona_juridica, documentos



import json as xjson
 


 

glbl_rut = ''

class usuarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = usuario
        fields = ['rut']
        """, 'email', 'direccion_calle', 'direccion_numero', 'comuna_cod_comu','perfil_id','fecha_creacion','fecha_modificacion','usuario_track'""" ,'usuario_track'

    def to_representation(self, instance):
        data = super(usuarioSerializer, self).to_representation(instance)
        print(data['rut'])
        print("*"*100)
        tengo_rut = data['rut']
        #-------------------------------------------------------------------------
        quiz_data3 = []
        sql3 = 'SELECT * FROM webapp_usuario where rut = "' + str(data['rut']) +'"'
        print(sql3)
        for table3 in usuario.objects.raw(sql3):
            quiz_data3.append({
                'rut': table3.rut,
                'ap_paterno': table3.ap_paterno,
                'ap_materno': table3.ap_materno
            })

        print(quiz_data3)
        print("*"*100)

        data['usuario'] = quiz_data3[0]    
        
        #-------------------------------------------------------------------------
        sql = 'SELECT * FROM webapp_persona_juridica_usuario where usuario_rut_id = "' + str(data['rut']) +'"'
        print(sql)
        glbl_quiz_data=[]
        for table1 in persona_juridica_usuario.objects.raw(sql):
            tipo = table1.tipo_participante_empresa_id_id
            sql2 = 'SELECT * FROM webapp_persona_juridica where rut = "' + str(table1.persona_juridica_rut_id) + '"'
            quiz_data = []
            for table2 in persona_juridica.objects.raw(sql2):
                quiz_data.append({
                    'rut': table2.rut,
                    'dv': table2.dv,
                    'razon_social': table2.razon_social,
                    "TIPO_RELACION": tipo
                })
                glbl_quiz_data.append(quiz_data[0])

        
        data['empresas'] = glbl_quiz_data
        
        #-------------------------------------------------------------------------

        data.update()
        return data


class persona_juridicaSearchd(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = usuarioSerializer
    def get_queryset(self):
        rutx =self.request.query_params.get('rut','')
        glbl_rut = rutx
        queryset = usuario.objects.filter(rut = rutx)
        
        return queryset



class set_usuario_empresa(APIView):
    #permission_classes = (IsAuthenticated,)
    def post(self, request):
        retorno = []
        empresa_request = request.data['empresa']
        usuario_request = request.data['usuario']

        usuario_rut = usuario_request['rut']
        usuario_rut = usuario_rut.split("-")
        rut = usuario_rut[0]
        dv = usuario_rut[1]

        empresa_rut = empresa_request['rut']
        empresa_rut = empresa_rut.split("-")
        rute = empresa_rut[0]
        dve = empresa_rut[1]


        """ usuario no ocupado
        telefono
        tipo_relacion
        nombres
        """
        try:
            instance = usuario.objects.filter(rut=rut)
            if instance.count() == 0:
                print("insertar usuario...")
                a = usuario(
                        rut = rut, 
                        rut_dv = dv, 
                        ap_paterno = usuario_request['ap_paterno'],
                        ap_materno = usuario_request['ap_materno'],
                        #email = usuario_request['email'],
                        cod_comuna_id = usuario_request['cod_comuna']
                    )
                a.save()
            #-----------persona jurida y documnto-----------------------
            instance = persona_juridica.objects.filter(rut=rute)
            if instance.count() == 0:
                #----------documento-----------------
                print("insertar documentos...")
                d = documentos(
                        nombre = empresa_request['nombre_documento']
                    )
                d.save()
                documentos_id = d.id
                #--------------------------                
                print("insertar persona_juridica...")
                b = persona_juridica(
                    rut = rute,
                    dv = dve,
                    razon_social = empresa_request['razon_social'],
                    comuna_cod_comuna_id = empresa_request['cod_comuna'],
                    direccion_via_id_id = int(empresa_request['via']),
                    acto_constitutivo_documentos_id_id = documentos_id
                )
                b.save()
            

            #--------------------------
            instance = persona_juridica_usuario.objects.filter(usuario_rut_id=rut, persona_juridica_rut=rute)
            if instance.count() == 0:
                print("insertar persona_juridica_usuario...")
                c = persona_juridica_usuario(
                    usuario_rut_id = int(rut),
                    persona_juridica_rut_id = int(rute),
                    tipo_participante_empresa_id_id = int(usuario_request['tipo_participante'])#,
                    #tipo='TITULAR'
                )
                c.save()

            #usuario_request['tipo_participante']

        except Exception as e:
            print(e)
            return Response("error: " + str(e))

        
        return Response("", status=status.HTTP_200_OK)
        
        
        



        

