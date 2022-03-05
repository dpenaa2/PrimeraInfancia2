from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Tipodiscapacidad(models.Model):
    idTipodiscapacidad = models.IntegerField(primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Tipodiscapacidad'


class Nacionalidad(models.Model):
    idpais = models.AutoField(db_column='idPais', primary_key=True)  # Field name made lowercase.
    codigopais = models.CharField(db_column='CodigoPais', max_length=3, blank=True,
                                  null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nacionalidad = models.CharField(db_column='Nacionalidad', max_length=20, blank=True,
                                    null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'nacionalidad'


class Regionales(models.Model):
    idregional = models.AutoField(db_column='idRegional', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.

    class Meta:
        verbose_name = 'regional'
        verbose_name_plural = 'regionales'
        managed = True
        db_table = 'regionales'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Municipios(models.Model):
    codigodane = models.CharField(db_column='CodigoDANE', primary_key=True, max_length=45)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    reg_idregional = models.ForeignKey('Regionales', on_delete=models.PROTECT,
                                       db_column='Reg_idRegional')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'municipios'


class CentroZonal(models.Model):
    idcentro_zonal = models.AutoField(db_column='idCentro_Zonal', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    mun_codigodane = models.ForeignKey('Municipios', on_delete=models.DO_NOTHING,
                                       db_column='Mun_CodigoDANE')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'centro_zonal'
        unique_together = (('idcentro_zonal', 'mun_codigodane'),)


class Grupoetnico(models.Model):
    idgrupoetnico = models.IntegerField(db_column='idGrupoEtnico', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'grupoetnico'


class Sexo(models.Model):
    idsexo = models.IntegerField(db_column='idSexo', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'sexo'


class Tipoidentificacio(models.Model):
    idtipoidentificacio = models.IntegerField(db_column='idTipoIdentificacio',
                                              primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tipoidentificacio'


class Lengua(models.Model):
    idlengua = models.IntegerField(db_column='idLengua', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    otralengua = models.CharField(db_column='OtraLengua', max_length=45, blank=True,
                                  null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'lengua'


class Persona(models.Model):
    idpersona = models.AutoField(db_column='idPersona', primary_key=True)
    no_documento = models.IntegerField(db_column='No_Documento', blank=True, null=True)  # Field name made lowercase.
    nombres = models.CharField(db_column='Nombres', max_length=50)  # Field name made lowercase.
    apellidos = models.CharField(db_column='Apellidos', max_length=50)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=45, blank=True,
                                null=True)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fecha_nacimiento = models.DateField(db_column='Fecha_Nacimiento', blank=False,
                                        null=False)  # Field name made lowercase.
    nacionalidad_idpais = models.ForeignKey(Nacionalidad, on_delete=models.DO_NOTHING,
                                            db_column='Nacionalidad_idPais')  # Field name made lowercase.
    cz_idcentro_zonal = models.ForeignKey(CentroZonal, on_delete=models.DO_NOTHING,
                                          db_column='CZ_idCentro_Zonal')  # Field name made lowercase.
    cz_mun_codigodane = models.ForeignKey(Municipios, on_delete=models.DO_NOTHING,
                                          db_column='CZ_Mun_CodigoDANE')  # Field name made lowercase.
    ge_idgrupoetnico = models.OneToOneField(Grupoetnico, on_delete=models.DO_NOTHING,
                                            db_column='GE_idGrupoEtnico')  # Field name made lowercase.
    sexo_idsexo = models.OneToOneField(Sexo, on_delete=models.DO_NOTHING,
                                       db_column='Sexo_idSexo')  # Field name made lowercase.
    tipoid_idtipoidentificacio = models.OneToOneField(Tipoidentificacio, on_delete=models.DO_NOTHING,
                                                      db_column='TipoId_idTipoIdentificacio')
    discapacidad = models.ManyToManyField(Tipodiscapacidad, through='TipodiscapacidadHasPersona')
    Lenguas = models.ManyToManyField(Lengua, through='LenguaHasPersona')

    class Meta:
        managed = True
        db_table = 'persona'
        unique_together = (('idpersona', 'cz_idcentro_zonal', 'cz_mun_codigodane'),)


class TipodiscapacidadHasPersona(models.Model):
    idTipodiscapacidad = models.ForeignKey(Tipodiscapacidad, on_delete=models.DO_NOTHING,
                                           db_column='idTipodiscapacidad')  # Field name made lowercase.
    idpersona = models.ForeignKey(Persona, on_delete=models.DO_NOTHING,
                                  db_column='idpersona')  # Field name made lowercase.
    idcentro_zonal = models.ForeignKey(CentroZonal, on_delete=models.DO_NOTHING,
                                       db_column='idcentro_zonal')  # Field name made lowercase.
    mun_codigodane = models.ForeignKey(Municipios, on_delete=models.DO_NOTHING,
                                       db_column='mun_codigodane')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Tipodiscapacidad_has_persona'
        unique_together = (
            ('idTipodiscapacidad', 'idpersona', 'idcentro_zonal', 'mun_codigodane'),)


class LenguaHasPersona(models.Model):
    len_idlengua = models.ForeignKey(Lengua, on_delete=models.DO_NOTHING,
                                     db_column='Len_idLengua')  # Field name made lowercase.
    idpersona = models.ForeignKey(Persona, on_delete=models.DO_NOTHING,
                                  db_column='idpersona')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'lengua_has_persona'
        unique_together = (('len_idlengua', 'idpersona'),)


class Remision(models.Model):
    idremision = models.AutoField(db_column='idRemision', primary_key=True)
    fechacrearemision = models.DateTimeField(db_column='FechaCreaRemision', auto_now_add=True)
    usucrearemision = models.IntegerField(db_column='UsuCreaRemision', blank=True, null=True)
    observacion = models.CharField(db_column='Observacion', max_length=500, blank=True, null=True)
    codigoremision = models.CharField(db_column='CodigoRemision', max_length=10, blank=True, null=True)
    idpersona = models.ForeignKey(Persona, on_delete=models.DO_NOTHING, db_column='idpersona')
    idcentro_zonal = models.ForeignKey(CentroZonal, on_delete=models.DO_NOTHING,
                                       db_column='idcentro_zonal')
    mun_codigodane = models.ForeignKey(Municipios, on_delete=models.DO_NOTHING,
                                       db_column='mun_codigodane')

    class Meta:
        managed = True
        db_table = 'remision'


class Remisioncatalogo(models.Model):
    idremisioncata = models.AutoField(db_column='idremisioncata',
                                      primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='codigo', max_length=10, blank=True,
                              null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rem_idremision = models.ForeignKey(Remision, on_delete=models.DO_NOTHING,
                                       db_column='Rem_idRemision')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'remisioncatalogo'


class Alertas(models.Model):
    idalertas = models.AutoField(db_column='idAlertas', primary_key=True)  # Field name made lowercase.
    nombrealerta = models.CharField(db_column='NombreAlerta', max_length=50, blank=True,
                                    null=True)  # Field name made lowercase.
    gradoalerta = models.IntegerField(db_column='GradoAlerta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'alertas'


class TipoModulo(models.Model):
    idtipo_modulo = models.IntegerField(db_column='idTipo_Modulo', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tipo_modulo'


class Seccion(models.Model):
    idseccion = models.AutoField(db_column='idSeccion', primary_key=True)  # Field name made lowercase.
    nombreseccion = models.CharField(db_column='NombreSeccion', max_length=45, blank=True,
                                     null=True)  # Field name made lowercase.
    tiposeccion = models.CharField(db_column='TipoSeccion', max_length=45, blank=True,
                                   null=True)  # Field name made lowercase.
    idtipo_modulo = models.ForeignKey(TipoModulo, on_delete=models.DO_NOTHING,
                                      db_column='idtipo_modulo')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'seccion'
        unique_together = (('idseccion', 'idtipo_modulo'),)


class Bitacora(models.Model):
    idbitacora = models.AutoField(db_column='idBitacora', primary_key=True)  # Field name made lowercase.
    fechacreacion = models.DateTimeField(db_column='FechaCreaRemision', auto_now_add=True)
    usuariocrea = models.IntegerField(db_column='UsuarioCrea', blank=True, null=True)  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=500, blank=True,
                                   null=True)  # Field name made lowercase.
    idpersona = models.ForeignKey(Persona, on_delete=models.DO_NOTHING,
                                  db_column='idpersona')  # Field name made lowercase.
    idcentro_zonal = models.ForeignKey(CentroZonal, on_delete=models.DO_NOTHING,
                                       db_column='idcentro_zonal')  # Field name made lowercase.
    mun_codigodane = models.ForeignKey(Municipios, on_delete=models.DO_NOTHING,
                                       db_column='mun_codigodane')  # Field name made lowercase.
    alertas = models.ManyToManyField(Alertas, through='BitacoraHasAlertas')

    class Meta:
        managed = True
        db_table = 'bitacora'
        unique_together = (('idbitacora', 'idpersona', 'idcentro_zonal', 'mun_codigodane'),)


class BitacoraHasAlertas(models.Model):
    bita_idbitacora = models.ForeignKey(Bitacora, on_delete=models.DO_NOTHING,
                                        db_column='Bita_idBitacora')  # Field name made lowercase.
    alert_idalertas = models.ForeignKey(Alertas, on_delete=models.DO_NOTHING,
                                        db_column='Alert_idAlertas')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'bitacora_has_alertas'
        unique_together = (('bita_idbitacora', 'alert_idalertas'),)


class Catalagopregunta(models.Model):
    idpregunta = models.AutoField(db_column='idPregunta', primary_key=True)  # Field name made lowercase.
    enunciado = models.CharField(db_column='Enunciado', max_length=250, blank=True,
                                 null=True)  # Field name made lowercase.
    codigopregunta = models.IntegerField(db_column='CodigoPregunta', blank=True,
                                         null=True)  # Field name made lowercase.
    sec_idseccion = models.ForeignKey(Seccion, on_delete=models.DO_NOTHING,
                                      db_column='Sec_idSeccion')  # Field name made lowercase.
    sec_idtipo_modulo = models.ForeignKey(TipoModulo, on_delete=models.DO_NOTHING,
                                          db_column='Sec_idtipo_modulo')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'catalagopregunta'
        unique_together = (('idpregunta', 'sec_idseccion', 'sec_idtipo_modulo'),)


class Catalogorespuestas(models.Model):
    idcatalogorespuestas = models.AutoField(db_column='idCatalogoRespuestas',
                                            primary_key=True)  # Field name made lowercase.
    tiporespuestas = models.CharField(db_column='TipoRespuestas', max_length=45, blank=True,
                                      null=True)  # Field name made lowercase.
    codigorespuestas = models.IntegerField(db_column='CodigoRespuestas', blank=True,
                                           null=True)  # Field name made lowercase.
    rta_otros = models.CharField(db_column='Rta_Otros', max_length=150, blank=True,
                                 null=True)  # Field name made lowercase.
    catapreg_idpregunta = models.ForeignKey(Catalagopregunta, on_delete=models.DO_NOTHING,
                                            db_column='CataPreg_idPregunta')  # Field name made lowercase.
    idseccion = models.ForeignKey(Seccion, on_delete=models.DO_NOTHING,
                                  db_column='idseccion')  # Field name made lowercase.
    sec_idtipo_modulo = models.ForeignKey(TipoModulo, on_delete=models.DO_NOTHING,
                                          db_column='sec_idtipo_modulo')

    class Meta:
        managed = True
        db_table = 'catalogorespuestas'
        unique_together = (('idcatalogorespuestas', 'catapreg_idpregunta', 'idseccion',
                            'sec_idtipo_modulo'),)


class Ficha(models.Model):
    idmodulo = models.AutoField(db_column='idModulo', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', auto_now_add=True)  # Field name made lowercase.
    idpersona = models.ForeignKey(Persona, models.DO_NOTHING,
                                  db_column='idpersona')  # Field name made lowercase.
    respuestas = models.ManyToManyField(Catalogorespuestas, through='FichaHasCatalogorespuestas')

    class Meta:
        managed = True
        db_table = 'ficha'


class FichaHasCatalogorespuestas(models.Model):
    ficha_idmodulo = models.OneToOneField(Ficha, models.DO_NOTHING, db_column='Ficha_idModulo',
                                          primary_key=True)  # Field name made lowercase.
    idcatalogorespuestas = models.ForeignKey(Catalogorespuestas, on_delete=models.DO_NOTHING,
                                             db_column='idcatalogorespuestas')
    catapreg_idpregunta = models.ForeignKey(Catalagopregunta, on_delete=models.DO_NOTHING,
                                            db_column='catapreg_idpregunta')
    catares_idseccion = models.ForeignKey(Seccion, on_delete=models.DO_NOTHING,
                                          db_column='CataRes_idseccion')
    catares_sec_idtipo_modulo = models.ForeignKey(TipoModulo, on_delete=models.DO_NOTHING,
                                                  db_column='CataRes_sec_idtipo_modulo')

    class Meta:
        managed = True
        db_table = 'ficha_has_catalogorespuestas'
        unique_together = (('ficha_idmodulo', 'idcatalogorespuestas', 'catapreg_idpregunta',
                            'catares_idseccion', 'catares_sec_idtipo_modulo'),)


class Grupofocal(models.Model):
    idgrupofocal = models.AutoField(db_column='idGrupoFocal', primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=50, blank=True, null=True)
    descripcion = models.CharField(db_column='Descripcion', max_length=500, blank=True,
                                   null=True)

    class Meta:
        managed = True
        db_table = 'grupofocal'


class Ong(models.Model):
    idong = models.AutoField(db_column='idONG', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=80, blank=True, null=True)  # Field name made lowercase.
    nit = models.IntegerField(db_column='NIT', blank=True, null=True)  # Field name made lowercase.
    digitoverificacion = models.IntegerField(db_column='DigitoVerificacion', blank=True,
                                             null=True)  # Field name made lowercase.
    representantelegal = models.CharField(db_column='RepresentanteLegal', max_length=50, blank=True,
                                          null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=45, blank=True,
                                 null=True)  # Field name made lowercase.
    telefono = models.IntegerField(db_column='Telefono', blank=True, null=True)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ong'


class Perfiles(models.Model):
    idperfilesroles = models.AutoField(db_column='idPerfilesRoles', primary_key=True)  # Field name made lowercase.
    codigopero = models.IntegerField(db_column='CodigoPERO', blank=True, null=True)  # Field name made lowercase.
    nombrepero = models.CharField(db_column='NombrePERO', max_length=30, blank=True,
                                  null=True)  # Field name made lowercase.
    usuariocrea = models.IntegerField(db_column='UsuarioCrea', blank=True, null=True)  # Field name made lowercase.
    usuariomodifica = models.IntegerField(db_column='UsuarioModifica', blank=True,
                                          null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'perfiles'


class PersonaHasGrupofocal(models.Model):
    idpersona = models.OneToOneField(Persona, models.DO_NOTHING, db_column='idpersona',
                                     primary_key=True)  # Field name made lowercase.
    idcentro_zonal = models.ForeignKey(CentroZonal, models.DO_NOTHING,
                                       db_column='idcentro_zonal')  # Field name made lowercase.
    mun_codigodane = models.ForeignKey(Municipios, models.DO_NOTHING,
                                       db_column='mun_codigodane')  # Field name made lowercase.
    gf_idgrupofocal = models.ForeignKey(Grupofocal, models.DO_NOTHING,
                                        db_column='GF_idGrupoFocal')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'persona_has_grupofocal'
        unique_together = (('idpersona', 'mun_codigodane', 'gf_idgrupofocal'),)


class Proyectos(models.Model):
    idproyectos = models.AutoField(db_column='idProyectos', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fechafin = models.DateField(db_column='FechaFin', blank=True, null=True)  # Field name made lowercase.
    fechainicio = models.DateField(db_column='FechaInicio', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=500, blank=True,
                                   null=True)  # Field name made lowercase.
    no_beneficiarios = models.IntegerField(db_column='No_Beneficiarios', blank=True,
                                           null=True)  # Field name made lowercase.
    tipo_proyecto = models.IntegerField(db_column='Tipo_Proyecto', blank=True, null=True)  # Field name made lowercase.
    ong_idong = models.ForeignKey(Ong, models.DO_NOTHING, db_column='ONG_idONG')  # Field name made lowercase.
    idsubdirecciones = models.ForeignKey('Subdirecciones', models.DO_NOTHING,
                                         db_column='idsubdirecciones')  # Field name made lowercase.
    gf_idgrupofocal = models.ForeignKey(Grupofocal, models.DO_NOTHING,
                                        db_column='GF_idGrupoFocal')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'proyectos'
        unique_together = (('idproyectos', 'idsubdirecciones', 'gf_idgrupofocal'),)


class Subdirecciones(models.Model):
    idsubdirecciones = models.AutoField(db_column='idSubDirecciones', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lider = models.CharField(db_column='Lider', max_length=45, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=45, blank=True,
                                 null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=45, blank=True,
                                null=True)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'subdirecciones'


class Uds(models.Model):
    iduds = models.AutoField(db_column='idUDS', primary_key=True)  # Field name made lowercase.
    codigocuentame = models.CharField(db_column='CodigoCuentame', max_length=30)  # Field name made lowercase.
    nombreagenteeducativo = models.CharField(db_column='NombreAgenteEducativo', max_length=50, blank=True,
                                             null=True)  # Field name made lowercase.
    fechacreacion = models.DateTimeField(db_column='FechaCreacion', blank=True, null=True)  # Field name made lowercase.
    ong_idong = models.ForeignKey(Ong, models.DO_NOTHING, db_column='ONG_idONG')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'uds'


class Funcionario(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    TIPO_DOCID = (
        ('1', 'CC'),
        ('2', 'CE'),
        ('3', 'PASAPORTE'),
        ('4', 'NIT'),
    )
    tipo_docid = models.CharField(max_length=1, choices=TIPO_DOCID)
    NoDocumento = models.TextField(max_length=500, blank=True)
    FechaNacimiento = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=60)

    class Meta:
        managed = True
        db_table = 'funcionario'
        unique_together = (('user', 'name'),)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Funcionario.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.funcionario.save()


class ProyectosHasUsuario(models.Model):
    idproyectos = models.OneToOneField(Proyectos, on_delete=models.DO_NOTHING, primary_key=True)
    idsubdirecciones = models.ForeignKey(Subdirecciones, models.DO_NOTHING)
    idgrupofocal = models.ForeignKey(Grupofocal, models.DO_NOTHING)
    User = models.ForeignKey(User, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'proyectos_has_usuarios'
        unique_together = (
            ('idproyectos', 'idsubdirecciones', 'idgrupofocal'),)
