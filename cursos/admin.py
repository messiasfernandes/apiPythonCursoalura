from django.contrib import admin

from cursos.models import Aluno, Curso, Matricula
@admin.register(Aluno)
class Alunos(admin.ModelAdmin):
    list_display=('id','nome','rg', 'cpf', 'data_de_nascimento')
    list_display_links=('id','nome')
    search_fields=('id','nome')
    list_per_page=10

@admin.register(Curso)
class Cursos(admin.ModelAdmin):
    list_display=('id','codigo_curso','descricao')
    list_display_links=('id','codigo_curso')
    search_fields=('id','codigo_curso')

@admin.register(Matricula)
class Matriculas(admin.ModelAdmin):
    list_display=('id','aluno','curso', 'periodo')
    list_display_links=('id',)
  ##  search_fields=('id','codigo_curso')