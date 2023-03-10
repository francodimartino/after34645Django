from django.db import models

# Create your models here.


class Curso(models.Model):
    nombre= models.CharField(max_length=50)
    comision=models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {str(self.comision)}"

class Estudiante(models.Model):
    nombre=models.CharField(max_length=60)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Profesor(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    profesion= models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Entregable(models.Model):
    nombre= models.CharField(max_length=50)
    fecha_entrega= models.DateField()
    entregado= models.BooleanField()


class Persona(models.Model):
    dni= models.IntegerField()
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    fechaNacimiento= models.DateField()
    tieneObraSocial= models.BooleanField()
    

    def __str__(self):
        return f"{self.nombre} {self.apellido}"