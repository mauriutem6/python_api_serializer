#---------------------------django---------------------------------------
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import simplejson as json
from django.contrib.auth.models import User
import json as xjson

#---------------------------local---------------------------------------
from . models import empresa
from . models import usuario, persona_juridica, persona_juridica_usuario

from . serializers import empresaSerializer
from . serializers import usuarioSerializer, persona_juridicaSerializer, persona_juridica_usuarioSerializer

from apimtt.settings import URL_SITIO

#----------------------------apiux----------------------------------------------
from webapp.api.comunas import ComunaSerializer, ComunaSearch



class obtenertoken(APIView):
    def post(self, request):
        retorno = {}
        
        code = request.data['code']
        state = request.data['state']
        

        try:
            import requests
            url = 'http://localhost:8080/openid-connect-server-webapp/token'
            form_data = [('client_secret', 'secret'), ('redirect_uri', 'http://localhost:3000/'), ('grant_type', 'authorization_code'), ('code', code), ('state', state), ('client_id', 'client')]
            r = requests.post(url, data=form_data)
            print(r.json())

            retorno['data_access_token'] = r.json()
            print("***********************************************************")
            data = r.json()
            auth_token = data['access_token']
        except Exception as e:
            print(e)
            return Response("1")


        hed = {'Authorization': 'Bearer ' + auth_token}
        data = {'app' : 'aaaaa'}
        url = 'http://localhost:8080/openid-connect-server-webapp/userinfo'

        try:
            response = requests.post(url, json=data, headers=hed)
            print(response)
            data2 = response.json()
            #csub = data2['sub']
            retorno['data_info'] = response.json()
        except Exception as e:
            print(e)
            return Response("2")

        json_registro_civil=""


        #-------------------------------------------django
        ###------------------------------------------------------------------
        #usuario de sistema
        xrut = '14905763'
        xpassword = 'passworsdsadasd'

        #-----------------jwt-----------------------------------------------
        
        instance = User.objects.filter(username=xrut)
        if instance.count() > 0:
            instance.delete()

        usuario = User.objects.create_user(username=xrut,
                                     email='mauriutem2@gmail.com',
                                     password=xpassword)
        #-------obtener un token por jwt django----------------------------
        import requests
        url = 'http://127.0.0.1:8000/api/token/'
        form_data = [('username', xrut), ('password', xpassword)]
        r = requests.post(url, data=form_data)
        print(r.json())
        retorno['data_tokenjwt'] = r.json()


        #request.session['tokenjwt'] = "123456"


        #--------------------------------------------------------------------


        return Response(retorno)
        
        #return Response("A")

class empresaList(APIView):
    def get(self, request):
        empresa1 = empresa.objects.all()
        serializer = empresaSerializer(empresa1, many=True)
        return Response(serializer.data)
        
    def post(self):
        pass


class get_usuario_empresas(APIView):
    def post(self, request):
        
        #print("comuna")
        #print(comuna)
        
        retorno = {}
        xrut = request.data['rut']
        print(xrut)
        
        #tokenjwt = request.session['tokenjwt']
        #print(request.session['tokenjwt'])
        tokenjwt = "77dc0d2ab2a523e9693343ff91b49f8f65d50122"
        print(tokenjwt)
        #data_tokenjwt = request.session['data_tokenjwt']
        print("hola2")
        url1 = "http://127.0.0.1:8000/db_usuario/"
        url2 = "http://127.0.0.1:8000/db_persona_juridica/"
        url3 = "http://127.0.0.1:8000/db_persona_juridica_usuario/"


        #---------------------------------------------------------
        hed = {'Authorization': 'Token ' + tokenjwt }
        data = {"rut": xrut}
        headers = {'content-type': 'application/json'}
        response = requests.post(url1, json=data, headers=hed)
        retorno['data_usuario'] = response.json()
        #---

        response = requests.post(url3, json=data, headers=hed)
        #retorno['url3'] = response.json()
        relacion = response.json() #relacion entre las tablas

        lista = {}
        contador = 0
        for x in relacion:
            print(x['persona_juridic'])
            print(x['tipo'])
            persona_juridic = x['persona_juridic']
            
            data = {"rut": persona_juridic}
            
            response = requests.post(url2, json=data, headers=hed)
            lista[contador] = response.json()
            
            contador=contador+1
        
        retorno['empresas'] = lista
        
        

        
        
        


        
        return Response(retorno)


#-------------------------------------------------------directo a db-----------------------------------------
class db_usuario(APIView):
    def post(self, request):
        xrut = request.data['rut']
        registros = usuario.objects.all()
        serializer = usuarioSerializer(registros, many=True)
        return Response(serializer.data)


class db_persona_juridica(APIView):
    def post(self, request):
        xrut = request.data['rut']
        registros = persona_juridica.objects.filter(rut=xrut)
        serializer = persona_juridicaSerializer(registros, many=True)
        return Response(serializer.data)


class db_persona_juridica_usuario(APIView):
    def post(self, request):
        xrut = request.data['rut']
        registros = persona_juridica_usuario.objects.all()
        serializer = persona_juridica_usuarioSerializer(registros, many=True)
        return Response(serializer.data)




