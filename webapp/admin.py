from django.contrib import admin
from . models import Region, Provincia, Comuna, periodo, flujo, vehiculos_equivalente, documentos, ficha
from . models import imiv, direccion_via, usuario, persona_juridica, tipo_participante_empresa, persona_juridica_usuario
from . models import uso_suelo, destino, dproyecto, rol, tipo_arteria, tipo_area, direccion_rol, proyecto, rol_proyecto
from . models import proyecto_ficha, proyecto_dproyecto, servicio_infraestructura, cant_periodo, log_proyecto
from . models import tasas_proyecto, tasas, persona_proyecto
admin.site.register(Region)
admin.site.register(Provincia)
admin.site.register(Comuna)
admin.site.register(periodo)
admin.site.register(flujo)
admin.site.register(vehiculos_equivalente)
admin.site.register(documentos)
admin.site.register(ficha)
admin.site.register(imiv)
admin.site.register(direccion_via)
admin.site.register(usuario)
admin.site.register(persona_juridica)
admin.site.register(tipo_participante_empresa)
admin.site.register(persona_juridica_usuario)
admin.site.register(uso_suelo)
admin.site.register(destino)
admin.site.register(dproyecto)
admin.site.register(rol)
admin.site.register(tipo_arteria)
admin.site.register(tipo_area)
admin.site.register(direccion_rol)
admin.site.register(proyecto)
admin.site.register(rol_proyecto)
admin.site.register(proyecto_ficha)
admin.site.register(proyecto_dproyecto)
admin.site.register(servicio_infraestructura)
admin.site.register(cant_periodo)
admin.site.register(log_proyecto)
admin.site.register(tasas_proyecto)
admin.site.register(tasas)
admin.site.register(persona_proyecto)

"""
from . models import empresa
from . models import usuario, persona_juridica, persona_juridica_usuario
from . models import Region, Provincia, Comuna

from . models import direccion_via
from . models import proyecto

from . models import log_proyecto, tipo_participante_empresa, documentos
from . models import dproyecto, destino, uso_suelo, vehiculos_equivalente

from . models import tipo_arteria, tipo_area
"""

# Register your models here.
#admin.site.register(empresa)
"""
admin.site.register(usuario)
admin.site.register(persona_juridica)
admin.site.register(persona_juridica_usuario)


admin.site.register(Region)
admin.site.register(Provincia)
admin.site.register(Comuna)




admin.site.register(direccion_via)
admin.site.register(proyecto)

admin.site.register(tipo_participante_empresa)
admin.site.register(log_proyecto)

admin.site.register(documentos)


admin.site.register(dproyecto)
admin.site.register(destino)
admin.site.register(uso_suelo)
admin.site.register(vehiculos_equivalente)



admin.site.register(tipo_arteria)
admin.site.register(tipo_area)
"""