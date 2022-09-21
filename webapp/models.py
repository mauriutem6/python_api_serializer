from django.db import models

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#--------------------
class Region(models.Model):
    codigo_region = models.CharField(max_length=200)
    region_ordinal = models.CharField(max_length=200, null=True)
    nombre = models.CharField(max_length=200)


    def __str__(self):
        return self.nombre
        

class Provincia(models.Model):
    region = models.ForeignKey(Region, related_name='provincias_region', on_delete=models.CASCADE)
    codigo_provincia = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)


    def __str__(self):
        return self.nombre


class Comuna(models.Model):
    provincia = models.ForeignKey(Provincia, related_name='comunas_provincia', on_delete=models.CASCADE)
    codigo_comuna = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)


    def __str__(self):
        return self.nombre

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#--------------------

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#---------------------------------- nuevos ------------------------------------------------------------------

class periodo(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=45, null=True, blank=True)

class flujo(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=45, null=True, blank=True)


class vehiculos_equivalente(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=45, null=True, blank=True)
    factor = models.CharField(max_length=45, null=True, blank=True)
    estado = models.CharField(max_length=1, null=True, blank=True)
    def __str__(self):
        retorno = "{0}-{1}.".format(self.id, self.nombre)
        return retorno




class documentos(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=45)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)
    #se debe cambiar data por documento    
    _data = models.TextField(
            db_column='data',
            blank=True)

    def set_data(self, data):
        self._data = base64.encodestring(data)

    def get_data(self):
        return base64.decodestring(self._data)

    data = property(get_data, set_data)

    def __str__(self):
        retorno = "{0}".format(self.nombre)
        return retorno

class ficha(models.Model):
    id = models.AutoField(primary_key = True)
    estado = models.CharField(max_length=45, null=True, blank=True)
    tipo_ficha = models.CharField(max_length=45, null=True, blank=True)
    certificado_documentos_id = models.ForeignKey(documentos, null=True, blank=True, related_name='creator',on_delete=models.CASCADE)
    oficiio_documentos_id = models.ForeignKey(documentos, null=True, blank=True, related_name='assignee',on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(null=True)




class imiv(models.Model):
    id = models.AutoField(primary_key = True)
    ficha_id = models.ForeignKey(ficha, related_name='imiv_ficha', on_delete=models.CASCADE)
    vigencia = models.DateTimeField(null=True)
    entrada_viajes = models.CharField(max_length=45, null=True, blank=True)
    salida_viajes = models.CharField(max_length=45, null=True, blank=True)
    entrada_vehiculo = models.CharField(max_length=45, null=True, blank=True)
    salida_vehiculos = models.CharField(max_length=45, null=True, blank=True)
    flujo_vehicular = models.CharField(max_length=45, null=True, blank=True)
    flujo_viajes = models.CharField(max_length=45, null=True, blank=True)
    categoria_flujo_vehicular = models.CharField(max_length=45, null=True, blank=True)
    categoria_flujo_viajes = models.CharField(max_length=45, null=True, blank=True)
    intersecciones_vehicular = models.CharField(max_length=45, null=True, blank=True)
    interseccionas_viajes = models.CharField(max_length=45, null=True, blank=True)
    area_influencia_vehicular = models.CharField(max_length=45, null=True, blank=True)
    area_influencia_viajes = models.CharField(max_length=45, null=True, blank=True)
    estado = models.CharField(max_length=1, null=True, blank=True)





class direccion_via(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=200)
    estado = models.CharField(max_length=1)
    
    def __str__(self):
        return '%d: %s' % (self.id, self.nombre)


class usuario(models.Model):
    rut = models.IntegerField(primary_key=True,null=False, blank=False)
    rut_dv = models.CharField(max_length=1, null=True, blank=True)
    
    nombres = models.CharField(max_length=45, null=True, blank=True)
    ap_paterno = models.CharField(max_length=45, null=True, blank=True)
    ap_materno = models.CharField(max_length=45, null=True, blank=True)
    direccion = models.CharField(max_length=45, null=True, blank=True)
    estado = models.CharField(max_length=45, null=True, blank=True)
    cod_comuna = models.ForeignKey(Comuna, related_name='usuario_comuna', on_delete=models.CASCADE)
    #consultar
    #---------------------esto no va---------------------------
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        retorno = "{0}-{1}.".format(self.rut, self.rut_dv)
        return retorno

class persona_juridica(models.Model):
    rut = models.IntegerField(primary_key=True,null=False, blank=False)
    dv = models.CharField(max_length=1, null=True, blank=True)
    razon_social = models.CharField(max_length=50, null=True, blank=True)
    direccion_via_id = models.ForeignKey(direccion_via, related_name='persona_juridica_direccion_via', on_delete=models.CASCADE)
    direccion = models.CharField(max_length=50, null=True, blank=True)
    direccion_numero = models.CharField(max_length=50, null=True, blank=True)
    direccion_depto = models.CharField(max_length=50, null=True, blank=True)    
    comuna_cod_comuna = models.ForeignKey(Comuna, related_name='persona_juridica_comuna', on_delete=models.CASCADE)
    acto_constitutivo_documentos_id = models.ForeignKey(documentos, related_name='persona_juridica_documentos', on_delete=models.CASCADE) #consultar documentos_id
    estado = models.CharField(max_length=1, null=True, blank=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        retorno = "{0} - {1}.".format(self.rut, self.razon_social)
        return retorno

class tipo_participante_empresa(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=45)

    def __str__(self):
        retorno = "{0} - {1}.".format(self.id, self.nombre)
        return retorno


class persona_juridica_usuario(models.Model):
    usuario_rut = models.ForeignKey(usuario, related_name='usuario_track', on_delete=models.CASCADE)
    persona_juridica_rut = models.ForeignKey(persona_juridica, related_name='persona_juridic_track', on_delete=models.CASCADE)
    tipo_participante_empresa_id = models.ForeignKey(tipo_participante_empresa, related_name='tipo_participante_empresa_secondary', on_delete=models.CASCADE)
    estado = models.CharField(max_length=1, null=True, blank=True)
    documento_legal_documentos_id = models.ForeignKey(
        documentos, 
        related_name='persona_juridica_usuario_documentos', 
        on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        unique_together = (("usuario_rut", "persona_juridica_rut","tipo_participante_empresa_id"),)
    def __str__(self):
        retorno = "{0}.".format(self.persona_juridica_rut)
        return retorno





class uso_suelo(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=45, null=True, blank=True)
    tipo = models.CharField(max_length=45, null=True, blank=True)
    def __str__(self):
        retorno = "{0}-{1}.".format(self.id, self.nombre)
        return retorno

class destino(models.Model):
    id = models.AutoField(primary_key = True)
    uso_suelo_id = models.ForeignKey(uso_suelo, related_name='uso_sueloSecondary', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=45, null=True, blank=True)
    tipo = models.CharField(max_length=45, null=True, blank=True)
    def __str__(self):
        retorno = "{0}-{1}.".format(self.id, self.nombre)
        return retorno
    

class dproyecto(models.Model):
    id = models.AutoField(primary_key = True)
    destino_id = models.ForeignKey(destino, related_name='destinoSecondary', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        retorno = "{0}-{1}.".format(self.id, self.nombre)
        return retorno






class rol(models.Model):
    id = models.AutoField(primary_key = True)
    rol = models.CharField(max_length=45, null=True, blank=True)




class tipo_arteria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=45, null=True, blank=True)
    estado = models.CharField(max_length=1, null=True, blank=True)
    def __str__(self):
        retorno = "{0}-{1}.".format(self.id, self.nombre)
        return retorno


class tipo_area(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=45, null=True, blank=True)
    estado = models.CharField(max_length=1, null=True, blank=True)
    def __str__(self):
        retorno = "{0}-{1}.".format(self.id, self.nombre)
        return retorno


class direccion_rol(models.Model):
    id = models.AutoField(primary_key = True)
    direccion = models.CharField(max_length=45, null=True, blank=True)
    numero = models.CharField(max_length=45, null=True, blank=True)
    rol_id = models.ForeignKey(rol, related_name='direccion_rol_rol', on_delete=models.CASCADE)
    direccion_via_id = models.ForeignKey(direccion_via, related_name='direccion_rol_direccion_via', on_delete=models.CASCADE)
    tipo_arteria_id = models.ForeignKey(tipo_arteria, related_name='direccion_rol_tipo_arteria', on_delete=models.CASCADE)
    tipo_area_id = models.ForeignKey(tipo_area, related_name='direccion_rol_tipo_area', on_delete=models.CASCADE)

    
class proyecto(models.Model):
    id = models.AutoField(primary_key = True)
    tipo_tramite = models.CharField(max_length=45, null=True, blank=True)
    nombre = models.CharField(max_length=45, null=True, blank=True)
    comuna_cod_comuna = models.ForeignKey(Comuna, related_name='proyecto_Comuna', on_delete=models.CASCADE)
    total_terreno = models.CharField(max_length=45, null=True, blank=True)
    superficie_util = models.CharField(max_length=45, null=True, blank=True)
    superficie_edificada = models.CharField(max_length=45, null=True, blank=True)
    rol_fusion = models.CharField(max_length=1, null=True, blank=True)
    ##proyecto_padre_id se apunta a si mismo opcional
    proyecto_padre_id = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    proposito = models.CharField(max_length=1, null=True, blank=True)
    tipo_crecimiento = models.CharField(max_length=1, null=True, blank=True)
    
    direccion_principal = models.ForeignKey(direccion_rol, related_name='proyecto_direccion_rol', on_delete=models.CASCADE)
    usuario_creador = models.ForeignKey(usuario, related_name='proyecto_usuario', on_delete=models.CASCADE)
    rut_pertenece = models.CharField(max_length=45, null=True, blank=True)
    descripcion = models.CharField(max_length=45, null=True, blank=True)
    colinda_camino_publico = models.CharField(max_length=1, null=True, blank=True)
    colinda_red_vial_basica = models.CharField(max_length=1, null=True, blank=True)
    estado = models.CharField(max_length=1, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return self.nombre


class rol_proyecto(models.Model):
    id = models.AutoField(primary_key = True)
    rol_id = models.ForeignKey(rol, related_name='rol_proyecto_rol', on_delete=models.CASCADE)
    proyecto_id = models.ForeignKey(proyecto, related_name='rol_proyecto_proyecto', on_delete=models.CASCADE)
    estado = models.CharField(max_length=1, null=True, blank=True)



class proyecto_ficha(models.Model):
    id = models.AutoField(primary_key = True)
    proyecto_id = models.ForeignKey(proyecto, related_name='proyecto_ficha_proyecto', on_delete=models.CASCADE)
    ficha_id = models.ForeignKey(ficha, related_name='proyecto_ficha_ficha', on_delete=models.CASCADE)
    declaracion_proy_conjunto_documentos_id = models.ForeignKey(documentos, null=True, blank=True, related_name='declaracion_proy_conjunto_documentos_id',on_delete=models.CASCADE)

class proyecto_dproyecto(models.Model):
    id = models.AutoField(primary_key = True)
    proyecto_id = models.ForeignKey(proyecto, related_name='proyecto_dproyecto_proyecto', on_delete=models.CASCADE)
    dproyecto_id = models.ForeignKey(dproyecto, related_name='proyecto_dproyecto_dproyecto', on_delete=models.CASCADE)
    
    cant_habitaciones = models.CharField(max_length=45, null=True, blank=True)
    num_habitaciones = models.CharField(max_length=45, null=True, blank=True)
    cant_personas = models.CharField(max_length=45, null=True, blank=True)
    cant_dispensadores = models.CharField(max_length=45, null=True, blank=True)
    num_asientos = models.CharField(max_length=45, null=True, blank=True)
    num_estudiantes = models.CharField(max_length=45, null=True, blank=True)
    num_viviendas = models.CharField(max_length=45, null=True, blank=True)
    num_estacionamientos = models.CharField(max_length=45, null=True, blank=True)
    num_lineas_revision = models.CharField(max_length=45, null=True, blank=True)
    num_darsenas = models.CharField(max_length=45, null=True, blank=True)
    total_servicios = models.CharField(max_length=45, null=True, blank=True)
    inc_servicios_movimiento = models.CharField(max_length=45, null=True, blank=True)
    escala = models.CharField(max_length=45, null=True, blank=True)

class servicio_infraestructura(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=45, null=True, blank=True)
    vehiculos_equivalente_id = models.ForeignKey(vehiculos_equivalente, related_name='servicio_infraestructura_vehiculos_equivalente', on_delete=models.CASCADE)
    proyecto_dproyecto_id = models.ForeignKey(proyecto_dproyecto, related_name='servicio_infraestructura_proyecto_dproyecto', on_delete=models.CASCADE)

class cant_periodo(models.Model):
    id = models.AutoField(primary_key = True)
    cant = models.CharField(max_length=45, null=True, blank=True)
    periodo_id = models.ForeignKey(periodo, related_name='cant_periodo_periodo', on_delete=models.CASCADE)
    servicio_infraestructura_id = models.ForeignKey(servicio_infraestructura, related_name='cant_periodo_servicio_infraestructura', on_delete=models.CASCADE)


#--------------------        


class log_proyecto(models.Model):
    id = models.AutoField(primary_key = True)
    proyecto_id = models.ForeignKey(proyecto, related_name='log_proyecto_proyecto', on_delete=models.CASCADE)
    usuario_rut = models.ForeignKey(usuario, related_name='log_proyecto_usuario', on_delete=models.CASCADE)
    observacion = models.CharField(max_length=45, null=True, blank=True)
    fecha = models.CharField(max_length=45, null=True, blank=True)



class tasas_proyecto(models.Model):
    id = models.AutoField(primary_key = True)
    tramo = models.CharField(max_length=45, null=True, blank=True)
    proyecto_dproyecto_id = models.ForeignKey(proyecto_dproyecto, related_name='tasas_proyecto_proyecto_dproyecto', on_delete=models.CASCADE)
    periodo_id = models.ForeignKey(periodo, related_name='tasas_proyecto_periodo', on_delete=models.CASCADE)
    tasa = models.CharField(max_length=45, null=True, blank=True)
    flujo_id = models.ForeignKey(flujo, related_name='tasas_proyecto_flujo', on_delete=models.CASCADE)
    fecha = models.DateTimeField(null=True)
    

class tasas(models.Model):
    id = models.AutoField(primary_key = True)
    tramo = models.CharField(max_length=45, null=True, blank=True)
    dproyecto_id = models.ForeignKey(dproyecto, related_name='tasas_dproyecto', on_delete=models.CASCADE)
    ##periodo_id no obligatoria
    periodo_id = models.ForeignKey(periodo, related_name='tasas_periodo', on_delete=models.CASCADE, blank=True, null=True)
    tasa = models.CharField(max_length=45, null=True, blank=True)
    flujo_id = models.ForeignKey(flujo, related_name='tasas_flujo', on_delete=models.CASCADE)
    fecha_vigencia = models.CharField(max_length=45, null=True, blank=True)
    estado = models.CharField(max_length=1, null=True, blank=True)



    







    
class persona_proyecto(models.Model):
    id = models.AutoField(primary_key = True)
    nombres = models.CharField(max_length=45, null=True, blank=True)
    ap_paterno = models.CharField(max_length=45, null=True, blank=True)
    ap_materno = models.CharField(max_length=45, null=True, blank=True)
    via = models.CharField(max_length=45, null=True, blank=True)
    direccion = models.CharField(max_length=45, null=True, blank=True)
    numero = models.CharField(max_length=45, null=True, blank=True)
    email = models.CharField(max_length=45, null=True, blank=True)
    telefono = models.CharField(max_length=45, null=True, blank=True)
    comuna_cod_comuna = models.ForeignKey(Comuna, related_name='persona_proyecto_comuna', on_delete=models.CASCADE)
    tipo_participante_empresa_id = models.ForeignKey(tipo_participante_empresa, related_name='persona_proyecto_tipo_participante_empresa', on_delete=models.CASCADE)
    proyecto_id = models.ForeignKey(proyecto, related_name='persona_proyecto_proyecto', on_delete=models.CASCADE)

    






#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#---------------------------------- nuevos ------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------




##---------------------------api-----------------------------------------------------------
#-----------------------modelo solicitado--------------------------------------------------
















    """
    estado = models.CharField(max_length=1, null=True, blank=True)
    #documento_legal_documentos_id

    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    """






#------------------------------------desde apix------------------------------------








#-------------------------------------------------------------------------------------------



# se debe quitar porque no esta en el modelo
class empresa(models.Model):
    id = models.AutoField(primary_key = True)
    rut = models.CharField('rut', max_length = 13)
    descripcion = models.CharField('descripcion', max_length = 200)
    ubicacion = models.CharField('ubicacion', max_length = 200)
    razon = models.CharField('razon', max_length = 200)
    def __str__(self):
        return '{0},{1}'.format(self.rut, self.descripcion)



