""""Descrição: Você vai criar um sistema simples de cadastro de usuários que armazena informações em uma lista e permite diversas
operações, como listar usuários, buscar um usuário por nome, calcular a média de idades, e remover usuários. O sistema deve usar
diferentes estruturas de controle e loops para realizar essas tarefas."""
"""
Menu de Opções:

O programa deve exibir um menu com as seguintes opções:
1 :Adicionar usuário
2:Listar usuários
3:Buscar usuário por nome
4:Calcular média de idades
5:Remover usuário
6:Sair


2:Adicionar Usuário:

*Solicite o nome e a idade do usuário.
*Armazene essas informações como um dicionário em uma lista.

3:Listar Usuários:

*Exiba todos os usuários cadastrados.
*Buscar Usuário por Nome:

4:Peça ao usuário um nome para busca.
*Use um loop para verificar se o nome está na lista.
*Se encontrado, exiba as informações do usuário.

5:Calcular Média de Idades:
*Use um loop para somar todas as idades e calcule a média.
*Exiba o resultado.

6:Remover Usuário:

*Solicite o nome do usuário a ser removido.
*Use um loop para encontrar e remover o usuário da lista.

7:Sair:

*Finalize o programa.
"""
"==================================================================================================================================================="

#------------------------------------------------------- Bloco das Importacoes---------------------------------------------------------------------

from datetime import date
dia_atual = date.today()     # variavel contendo o dia atual





#----------------------------------------------------------Bloco das Funções------------------------------------------------------------------------


def adicionar_usuario():
    """adiciona usuario a uma lista """""               # -> DOC STR
    pass

def listar_usuario():
    """Busca todos usuarios da lista """""
    pass

def buscar_usuario():
    """Busca um usuario especifico da lista"""
    pass

def calcular_media_idade():
    """Calcula a media  das idades inseridas nas listas """
    pass

def remover_usuario():
    """Remova usuario especifico de uma lista"""
    def remove_todos():
        """Remova todos os usuarios de uma so vez """
        pass

def sair():
    """Finalizar a execucao"""
    pass

#------------------------------------------------------ Body Code-----------------------------------------------------------------------------
print(3*""
        
      "")
print(25*"-_-","MENU DE OPÇÕES",25*"-_-")

print(
    """
    1 :Adicionar usuário
    2:Listar usuários
    3:Buscar usuário por nome
    4:Calcular média de idades
    5:Remover usuário
    6:Sair
    """
)
tigger = 0
while True:
    try:
        tigger = int(input("Escolha umas das Opções acima:"))
        if tigger <= 0 or tigger <= 7:
            break
        else:
            print("Escolha um numero entre 1 e 6 ")


    except:
        print(7*"-","Erro ao digitar  -_-",7*"-")
        print("Desculpe ! Letras,Simbolos e Numeros Reais nao são aceitos na operação")
        print("----------------------------------------------------------")
        print(5*"->","Tente Novamente!",5*"<-")


if tigger == 1:
    print("Adicionar Usuario")
    adicionar_usuario()
elif tigger == 2:
    print("Listar Usuario")
    listar_usuario()
elif tigger == 3:
    print("Buscar usuario")
    buscar_usuario()
elif tigger == 4:
    print("Calcular media")
    calcular_media_idade()
elif tigger == 5:
    print("Remover usuario")
    remover_usuario()
elif tigger == 6:
    print("Sair do programa")










