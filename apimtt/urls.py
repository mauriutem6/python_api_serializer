"""apimtt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path

from webapp import views
#from rest_framework.authtoken import views as authviews

from webapp.api.comunas import ComunaView, ComunaSearch, IntanciaComunaDetailView
from rest_framework import routers
from django.urls import path
from rest_framework_simplejwt import views as jwt_views





from webapp.api.usuario import IntanciausuarioView

from webapp.api.persona_juridica_usuariod import persona_juridica_usuarioSearchd
from webapp.api.persona_juridica import persona_juridicaSearchd
from webapp.api.persona_juridica import set_usuario_empresa
from webapp.api.direccion_via import get_direccion_via
from webapp.api.regiones import RegionProvinciasView, RegionView
from webapp.api.proyecto import get_proyectoall, get_proyectoe3

from webapp.api.vehiculos_equivalente import get_vehiculos_equivalente

from webapp.api.tipo_area import get_tipo_area

from webapp.api.tipo_arteria import get_tipo_arteria




router = routers.SimpleRouter()
router.register('api/regiones', RegionProvinciasView, 'list-regiones')
router.register(r'api/regiones-all', RegionView, 'regiones')

urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
    #------------------------------------------login------------------------------------------
    path('admin/', admin.site.urls),
    path('empresaList/', views.empresaList.as_view()),
    #path('api_generate_token/', authviews.obtain_auth_token),
    path('obtenertoken/', views.obtenertoken.as_view()),

    path('api/set_usuario_empresa', set_usuario_empresa.as_view()),

    
    #-----
    path('api/vehiculos_equivalente/', get_vehiculos_equivalente.as_view({'get': 'list'}), name='get_vehiculos_equivalente'),

    
    path('api/tipos_area/', get_tipo_area.as_view({'get': 'list'}), name='get_tipo_area'),
    path('api/tipos_arteria/', get_tipo_arteria.as_view({'get': 'list'}), name='get_tipo_arteria'),
    
    

    #------------------------------------------vistas------------------------------------------
    path('get_usuario_empresas/' , views.get_usuario_empresas.as_view()),

    

    

    #------------------------------------------dbs------------------------------------------
    path('db_usuario/', views.db_usuario.as_view()),
    path('db_persona_juridica/', views.db_persona_juridica.as_view()),
    path('db_persona_juridica_usuario/', views.db_persona_juridica_usuario.as_view()),
    
    #---------------------------------------------apiux---------------------------------------
    path('api/ComunaSearch/', ComunaSearch.as_view({'get': 'list'}), name='ComunaSearch'),    
    #path('api/regiones/', RegionProvinciasView.as_view({'get': 'list'}), name='ComunaSearch'),    

    path('api/persona_juridica_usuarioSearchd/', persona_juridica_usuarioSearchd.as_view({'get': 'list'}), name='track-filter'),    
    path('api/persona_juridicaSearchd/', persona_juridicaSearchd.as_view({'get': 'list'}), name='persona_juridicaSearchd'),
    path('api/direccion_vias/', get_direccion_via.as_view({'get': 'list'}), name='get_direccion_via'),


    path('api/proyectos/', get_proyectoall.as_view({'get': 'list'}), name='get_proyectoall_view'),
    path('api/proyectoso3/', get_proyectoe3.as_view({'get': 'list'}), name='get_proyectoall_view'),

    path('api/instanciacomuna/<str:pk>/', IntanciaComunaDetailView.as_view(), name='instancia_comuna'),

    path('api/IntanciausuarioView/<str:pk>/', IntanciausuarioView.as_view(), name='IntanciausuarioView'),    
]

urlpatterns += router.urls 
