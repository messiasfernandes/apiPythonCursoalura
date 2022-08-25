from dataclasses import fields
from rest_framework import serializers
from cursos.models import Aluno, Curso,Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model =Aluno
        fields=['id','nome','rg', 'cpf', 'data_de_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Curso
        fields='__all__'
            
class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Matricula
        exclude=[]

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    aluno = serializers.ReadOnlyField(source='aluno.nome')
    cpf = serializers.ReadOnlyField(source='aluno.cpf')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['curso', 'periodo','aluno','cpf']
    
    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
     model = Matricula
     fields = ['curso','aluno_nome']