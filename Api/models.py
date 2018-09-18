# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Ciudad(models.Model):
    id_ciudad = models.AutoField(primary_key=True)
    departamento = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ciudad'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    nit = models.IntegerField(blank=True, null=True)
    id_tipo = models.ForeignKey('Tipo', models.DO_NOTHING, db_column='id_tipo', blank=True, null=True)
    id_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='id_ciudad', blank=True, null=True)
    direccion = models.CharField(max_length=25, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    celular = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    logo = models.CharField(max_length=20, blank=True, null=True)
    lema = models.CharField(max_length=200, blank=True, null=True)
    mision = models.CharField(max_length=400, blank=True, null=True)
    vision = models.CharField(max_length=400, blank=True, null=True)
    nombre_ser_1 = models.CharField(max_length=100, blank=True, null=True)
    ser_1 = models.CharField(max_length=400, blank=True, null=True)
    nombre_ser_2 = models.CharField(max_length=100, blank=True, null=True)
    ser_2 = models.CharField(max_length=400, blank=True, null=True)
    nombre_ser_3 = models.CharField(max_length=100, blank=True, null=True)
    ser_3 = models.CharField(max_length=400, blank=True, null=True)
    nombre_ser_4 = models.CharField(max_length=100, blank=True, null=True)
    ser_4 = models.CharField(max_length=400, blank=True, null=True)
    nombre_ser_5 = models.CharField(max_length=100, blank=True, null=True)
    ser_5 = models.CharField(max_length=400, blank=True, null=True)
    fecha_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresa'


class RegistrationRegistrationprofile(models.Model):
    activation_key = models.CharField(max_length=40)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'registration_registrationprofile'


class Tipo(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo'


class Users(models.Model):
    nombre = models.TextField()
    apellido = models.TextField()
    correo = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'users'

class Empresas_view(models.Model):
    id_empresa = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    email_user = models.CharField(max_length=254)
    nit = models.IntegerField(blank=True, null=True)
    ciudad = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    direccion = models.CharField(max_length=25)
    telefono = models.IntegerField(blank=True, null=True)
    celular = models.IntegerField(blank=True, null=True)
    logo = models.CharField(max_length=20, blank=True, null=True)
    lema = models.CharField(max_length=200, blank=True, null=True)
    nombre_ser_1 = models.CharField(max_length=100, blank=True, null=True)
    ser_1 = models.CharField(max_length=400, blank=True, null=True)
    nombre_ser_2 = models.CharField(max_length=100, blank=True, null=True)
    ser_2 = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        db_table = 'empresas_view'
        managed = False
        # verbose_name = 'ModelName'
        # verbose_name_plural = 'ModelNames'

