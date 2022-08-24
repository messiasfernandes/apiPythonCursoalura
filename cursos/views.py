from rest_framework import viewsets
from cursos.models import Curso,Aluno,Matricula
from cursos.serializer import AlunoSerializer, CursoSerializer,MatriculaSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunoas """
    queryset= Aluno.objects.all()
    serializer_class = AlunoSerializer



class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Cursos"""
    queryset=Curso.objects.all()
    serializer_class=CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Matrículas"""
    queryset=Matricula.objects.all()
    serializer_class=MatriculaSerializer