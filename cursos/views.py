from rest_framework import viewsets, generics
from cursos.models import Curso,Aluno,Matricula
from cursos.serializer import AlunoSerializer, CursoSerializer,MatriculaSerializer, ListaMatriculasAlunoSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunoas """
    queryset= Aluno.objects.all()
    serializer_class = AlunoSerializer



class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Cursos"""
    queryset=Curso.objects.all()
    serializer_class=CursoSerializer

class MatriulaViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Matriculas"""
    queryset=Matricula.objects.all()
    serializer_class=MatriculaSerializer

class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matrículas de aluna e aluno"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer