
from django.contrib import admin
from django.urls import path, include
from cursos.views import AlunosViewSet, CursosViewSet, MatriulaViewSet,ListaMatriculasAluno
from rest_framework import routers

router =routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matriculas', MatriulaViewSet, basename='Matriculas')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('aluno/<int:pk>/matriculas/',ListaMatriculasAluno.as_view()),
]
