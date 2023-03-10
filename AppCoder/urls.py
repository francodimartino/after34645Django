from django.urls import path
from .views import *



urlpatterns = [
    path("curso/", curso),
    path("cursos/", cursos, name="cursos"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("profesores/", profesores, name="profesores"),
    path("entregables/", entregables, name="entregables"),
    path("", inicio, name="inicio"),

    path("cursoFormulario/", cursoFormulario, name="cursoFormulario"),
    path("profeFormulario/", profeFormulario, name="profeFormulario"),
    path("busquedaComision/", busquedaComision, name="busquedaComision"),
    path("buscar/", buscar, name="buscar"),

    path("leerProfesores/", leerProfesores, name="leerProfesores"),
    path("eliminarProfesor/<id>", eliminarProfesor, name="eliminarProfesor"),
    path("editarProfesor/<id>", editarProfesor, name="editarProfesor"),

    path("estudiante/list/", EstudianteList.as_view(), name="estudiante_list"),
    path('estudiante/nuevo/', EstudianteCreacion.as_view(), name='estudiante_crear'),
    path('estudiante/<pk>', EstudianteDetalle.as_view(), name='estudiante_detalle'),
    path('estudiante/borrar/<pk>', EstudianteDelete.as_view(), name='estudiante_borrar'),
    path('estudiante/editar/<pk>', EstudianteUpdate.as_view(), name='estudiante_editar'),

    path("leerPersonas/", leerPersonas, name="leerPersonas"),
    path("agregarPersona/", agregarPersona, name="agregarPersona"),
    path("editarPersona/<id>", editarPersona, name="editarPersona"),
    path("eliminarPersona/<id>", eliminarPersona, name="eliminarPersona"),


]