from django.db import models
from datetime import datetime
from django.forms import model_to_dict
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Tipodiscapacidad(models.Model):
    idTipodiscapacidad = models.AutoField(db_column='idTipodiscapacidad',
                                          primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True, unique=True)
    ESTADO_ID = (
        ('1', 'Activo'),
        ('2', 'Inactivo'),
    )
    estado = models.CharField(max_length=1, choices=ESTADO_ID, default=1)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = True
        db_table = 'Tipodiscapacidad'


class Nacionalidad(models.Model):
    idpais = models.AutoField(db_column='idPais', primary_key=True)
    Pais = models.CharField(db_column='Pais', max_length=30, blank=True, null=True, unique=True)
    nacionalidad = models.CharField(db_column='Nacionalidad', max_length=20, blank=True,
                                    null=True, unique=True)

    def __str__(self):
        return self.nacionalidad

    class Meta:
        managed = True
        db_table = 'nacionalidad'


class Regionales(models.Model):
    idregional = models.AutoField(db_column='idRegional', primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=45, unique=True)
    ESTADO_ID = (
        ('1', 'Activo'),
        ('2', 'Inactivo'),
    )
    estado = models.CharField(max_length=1, choices=ESTADO_ID, default=1)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'regional'
        verbose_name_plural = 'regionales'
        managed = True
        db_table = 'regionales'
        ordering = ['nombre']


class Municipios(models.Model):
    codigodane = models.CharField(db_column='CodigoDANE', primary_key=True, max_length=45)
    nombre = models.CharField(db_column='Nombre', max_length=50, blank=True, null=False, unique=True)
    Regional = models.ForeignKey('Regionales', on_delete=models.PROTECT,
                                 db_column='Reg_idRegional')

    def __str__(self):
        return self.nombre

    ESTADO_ID = (
        ('1', 'Activo'),
        ('2', 'Inactivo'),
    )
    estado = models.CharField(max_length=1, choices=ESTADO_ID, default=1)

    class Meta:
        managed = True
        db_table = 'municipios'


class CentroZonal(models.Model):
    idcentro_zonal = models.AutoField(db_column='idCentro_Zonal', primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=45, unique=True)
    municipio = models.ForeignKey('Municipios', on_delete=models.DO_NOTHING, db_column='Mun_CodigoDANE')
    ESTADO_ID = (
        ('1', 'Activo'),
        ('2', 'Inactivo'),
    )
    estado = models.CharField(max_length=1, choices=ESTADO_ID, default=1)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = True
        db_table = 'centro_zonal'
        unique_together = (('idcentro_zonal', 'municipio'),)


class GruposEtnicos(models.Model):
    idgrupoetnico = models.AutoField(db_column='idGrupoEtnico', primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = True
        db_table = 'GruposEtnicos'
        unique_together = (('idgrupoetnico', 'nombre'),)


class Sexo(models.Model):
    idsexo = models.AutoField(db_column='idSexo', primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = True
        db_table = 'sexo'


class Tipoidentificacio(models.Model):
    idtipoidentificacio = models.AutoField(db_column='idTipoIdentificacio', primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = True
        db_table = 'tipoidentificacio'


class Lengua(models.Model):
    idlengua = models.AutoField(db_column='idLengua', primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True, unique=True)
    otralengua = models.CharField(db_column='OtraLengua', max_length=45, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = True
        db_table = 'lengua'


class Persona(models.Model):
    idpersona = models.AutoField(db_column='idPersona', primary_key=True)
    idtipoidentificacio = models.ForeignKey('Tipoidentificacio', models.DO_NOTHING,
                                            db_column='TipoId_idTipoIdentificacio')
    no_documento = models.IntegerField(db_column='No_Documento', blank=True, null=True)
    nombres = models.CharField(db_column='Nombres', max_length=50)
    apellidos = models.CharField(db_column='Apellidos', max_length=50)
    idsexo = models.ForeignKey('Sexo', models.DO_NOTHING, db_column='Sexo_idSexo')
    fecha_nacimiento = models.DateField(db_column='Fecha_Nacimiento', blank=False, null=False)
    nacionalidades = models.ManyToManyField(Nacionalidad,
                                            through='NacionalidadPersona',
                                            through_fields=('persona', 'nacionalidad'),
                                            )
    idcentro_zonal = models.ForeignKey(CentroZonal, models.DO_NOTHING, db_column='CZ_idCentro_Zonal')
    mun_codigodane = models.ForeignKey(Municipios, models.DO_NOTHING, db_column='CZ_Mun_CodigoDANE')
    direccion = models.CharField(db_column='Direccion', max_length=45, blank=True, null=True)
    idgrupoetnico = models.ForeignKey(GruposEtnicos, models.DO_NOTHING, db_column='Grupoetnico_idGrupoetnico')
    discapacidades = models.ManyToManyField(Tipodiscapacidad,
                                            through='TipodiscapacidadPersona',
                                            through_fields=('persona', 'tipodiscapacidad'),
                                            )
    lenguas = models.ManyToManyField(Lengua,
                                     through='LenguaPersona',
                                     through_fields=('persona', 'lengua'),
                                     )
    telefono = models.CharField(db_column='Telefono', max_length=45, blank=True, null=True)
    correo = models.CharField(db_column='Correo', max_length=45, blank=True, null=True)
    ESTADO_ID = (
        ('0', 'PreAprobado'),
        ('1', 'Aprobado'),
        ('2', 'Inactivo'),
    )
    estado = models.CharField(max_length=1, choices=ESTADO_ID, default=1)

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return '{} {} / {}'.format(self.nombres, self.apellidos, self.no_documento)

    class Meta:
        managed = True
        db_table = 'persona'


class TipodiscapacidadPersona(models.Model):
    tipodiscapacidad = models.ForeignKey(Tipodiscapacidad, on_delete=models.CASCADE, db_column='idtipodiscapacidad')
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, db_column='persona')

    def __str__(self):
        return self.tipodiscapacidad

    class Meta:
        managed = True
        db_table = 'tipodiscapasidad_persona'
        unique_together = (('tipodiscapacidad', 'persona'),)


class NacionalidadPersona(models.Model):
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE, db_column='idnacionalidad')
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, db_column='idpersona')

    def __str__(self):
        return self.nacionalidad

    class Meta:
        managed = True
        db_table = 'nacionalidad_persona'
        unique_together = (('nacionalidad', 'persona'),)


class LenguaPersona(models.Model):
    lengua = models.ForeignKey(Lengua, on_delete=models.CASCADE, db_column='lengua')
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, db_column='persona')

    def __str__(self):
        return self.lengua

    class Meta:
        managed = True
        db_table = 'lengua_persona'
        unique_together = (('lengua', 'persona'),)


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
        instance.funcionario.save(),


class TipoModulo(models.Model):
    idtipo_modulo = models.AutoField(db_column='idTipo_Modulo', primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)
    ESTADO_ID = (
        ('1', 'Activo'),
        ('2', 'Inactivo'),
    )
    estado = models.CharField(max_length=1, choices=ESTADO_ID, default=1)

    def __str__(self):
        return str(self.nombre)

    class Meta:
        managed = True
        db_table = 'nombre'


class Seccion(models.Model):
    idseccion = models.AutoField(db_column='idSeccion', primary_key=True)
    nombre_seccion = models.CharField(db_column='NombreSeccion', max_length=45, blank=True,
                                      null=True)
    SECCION_ID = (
        ('1', 'Principal'),
        ('2', 'Secundaria'),
    )
    tiposeccion = models.CharField(max_length=1, choices=SECCION_ID, default=1)
    idtipo_modulo = models.ForeignKey(TipoModulo, on_delete=models.DO_NOTHING,
                                      db_column='idtipo_modulo')
    ESTADO_ID = (
        ('1', 'Activo'),
        ('2', 'Inactivo'),
    )
    estado = models.CharField(max_length=1, choices=ESTADO_ID, default=1)

    def __str__(self):
        return str(self.nombre_seccion)

    class Meta:
        managed = True
        db_table = 'seccion'
        unique_together = (('idseccion', 'nombre_seccion'),)


class Catalagopregunta(models.Model):
    idpregunta = models.AutoField(db_column='idPregunta', primary_key=True)
    enunciado = models.CharField(db_column='Enunciado', max_length=250, blank=True,
                                 null=True)
    codigopregunta = models.IntegerField(db_column='CodigoPregunta', blank=True,
                                         null=True)
    sec_idseccion = models.ForeignKey(Seccion, on_delete=models.DO_NOTHING,
                                      db_column='Sec_idSeccion')
    sec_idtipo_modulo = models.ForeignKey(TipoModulo, on_delete=models.DO_NOTHING,
                                          db_column='Sec_idtipo_modulo')

    def __str__(self):
        return str(self.enunciado)

    class Meta:
        managed = True
        db_table = 'catalagopregunta'
        unique_together = (('idpregunta', 'sec_idseccion', 'sec_idtipo_modulo'),)


class Catalogorespuestas(models.Model):
    idcatalogorespuestas = models.AutoField(db_column='idCatalogoRespuestas',
                                            primary_key=True)
    tipo_respuestas = models.CharField(db_column='TipoRespuestas', max_length=45, blank=True,
                                       null=True)
    codigo_respuestas = models.IntegerField(db_column='CodigoRespuestas', blank=True,
                                            null=True)
    catapreg_idpregunta = models.ForeignKey(Catalagopregunta, on_delete=models.DO_NOTHING,
                                            db_column='CataPreg_idPregunta')
    idseccion = models.ForeignKey(Seccion, on_delete=models.DO_NOTHING,
                                  db_column='idseccion')
    sec_idtipo_modulo = models.ForeignKey(TipoModulo, on_delete=models.DO_NOTHING,
                                          db_column='sec_idtipo_modulo')

    def __str__(self):
        return str(self.tipo_respuestas)

    class Meta:
        managed = True
        db_table = 'catalogorespuestas'
        unique_together = (('idcatalogorespuestas', 'catapreg_idpregunta', 'idseccion',
                            'sec_idtipo_modulo'),)


class Ficha(models.Model):
    idficha = models.AutoField(db_column='idficha', primary_key=True)
    fecha = models.DateField(db_column='Fecha', auto_now_add=True)
    idpersona = models.ForeignKey(Persona, models.DO_NOTHING,
                                  db_column='idpersona')
    respuestas = models.ManyToManyField(Catalogorespuestas,
                                        through='FichaRespuestas',
                                        through_fields=('idFicha', 'idrespuestas', 'idpregunta', 'idseccion',
                                                        'idtipo_modulo'), )

    def __str__(self):
        return self.idficha

    class Meta:
        managed = True
        db_table = 'ficha'


class FichaRespuestas(models.Model):
    idFicha = models.ForeignKey(Ficha, on_delete=models.CASCADE, db_column='idFicha')

    idrespuestas = models.ForeignKey(Catalogorespuestas, on_delete=models.DO_NOTHING,
                                     db_column='idrespuestas')
    idpregunta = models.ForeignKey(Catalagopregunta, on_delete=models.DO_NOTHING,
                                   db_column='idpregunta')
    idseccion = models.ForeignKey(Seccion, on_delete=models.DO_NOTHING,
                                  db_column='idseccion')
    idtipo_modulo = models.ForeignKey(TipoModulo, on_delete=models.DO_NOTHING,
                                      db_column='idtipo_modulo')

    def __str__(self):
        return self.idFicha

    class Meta:
        managed = True
        db_table = 'FichaRespuestas'
        unique_together = (('idFicha', 'idrespuestas', 'idpregunta',
                            'idseccion', 'idtipo_modulo'),)
