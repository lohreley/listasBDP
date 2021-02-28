from django.db import models

# Create your models here.
class Persona(models.Model):
    idPersona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=15)
    telefono = models.CharField(max_length=20)
    mail = models.CharField(max_length=50)

    def nombreCompleto(self):
        txt = "{0}, {1}"
        return txt.format(self.apellido, self.nombre)

class Admin(models.Model):
    idAdmin = models.AutoField(primary_key=True)
    idPersona = models.ForeignKey(Persona, null=False, blank=False, on_delete=models.DO_NOTHING)

class Jefe(models.Model):
    idJefe = models.AutoField(primary_key=True)
    idAdmin = models.ForeignKey(Admin, null=False, blank=False, on_delete=models.DO_NOTHING)
    idPersona = models.ForeignKey(Persona, null=False, blank=False, on_delete=models.DO_NOTHING)

class Cordinador(models.Model):
    idCordinador = models.AutoField(primary_key=True)
    idPersona = models.ForeignKey(Persona, null=False, blank=False, on_delete=models.DO_NOTHING)

class List(models.Model):
    idList = models.AutoField(primary_key=True)
    idCordinador = models.ForeignKey(Cordinador, null=False, blank=False, on_delete=models.DO_NOTHING)

class Supervisa(models.Model):
    idJefe = models.AutoField(primary_key=True)
    idCordinador = models.ForeignKey(Cordinador, null=False, blank=False, on_delete=models.DO_NOTHING)

class Presente(models.Model):
    idPresente = models.AutoField(primary_key=True)
    idPersona = models.ForeignKey(Persona, null=False, blank=False, on_delete=models.DO_NOTHING)
    idLista = models.ForeignKey(List, null=False, blank=False, on_delete=models.DO_NOTHING)
    fecha = models.DateField()
    presente = [
        ('p', 'presente'),
        ('a', 'ausente'),
        ('j', 'justificado')
    ]
    presente = models.CharField(max_length=1, choices=presente, default='a')