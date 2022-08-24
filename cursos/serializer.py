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
        fields='__all__'
       ## exclude=[]