from django.contrib import admin
from .models import Curso, Estudiante, Profesor, Entregable, Persona

# Register your models here.
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Entregable)
admin.site.register(Persona)