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


1:Adicionar Usuário:

*Solicite o nome e a idade do usuário.
*Armazene essas informações como um dicionário em uma lista.

2:Listar Usuários:

*Exiba todos os usuários cadastrados.
*Buscar Usuário por Nome:

3:Peça ao usuário um nome para busca.
*Use um loop para verificar se o nome está na lista.
*Se encontrado, exiba as informações do usuário.

4:Calcular Média de Idades:
*Use um loop para somar todas as idades e calcule a média.
*Exiba o resultado.

5:Remover Usuário:

*Solicite o nome do usuário a ser removido.
*Use um loop para encontrar e remover o usuário da lista.

6:Sair:

*Finalize o programa.
"""
"==================================================================================================================================================="

#------------------------------------------------------- Bloco das Importacoes---------------------------------------------------------------------

from datetime import date
dia_atual = date.today()     # variavel contendo o dia atual


#*Solicite o nome e a idade do usuário.
#*Armazene essas informações como um dicionário em uma lista.


#----------------------------------------------------------Bloco das Funções------------------------------------------------------------------------

lista_dados_usuarios = []
def adicionar_usuario():
    """adiciona usuario a uma lista """""
    nome = input("Digite seu nome:")
    nome_valido = trata_strs(nome)                      # Funcao ja esta tratando entrada digitada pelo usuario
    idade = input("Digite sua idade:")
    idade_valida = trata_int(idade)                      # Funcao ja esta tratando entrada digitada pelo usuario

    dict_geral = {"nome":nome_valido,"idade":idade_valida}        #Adiciona entrada digitada pelo usuario detreww de um dicionario
    lista_dados_usuarios.append(dict_geral)         #Adiciona o dicionanario dentro de um lista




    print("Adicionado com sucesso")






def listar_usuario():
    """Busca todos usuarios da lista """""
    for dicionario in lista_dados_usuarios:
        for dict_nome, dict_idade in dicionario.items():
            print(f"{dict_nome}:{dict_idade}")
    print(20 * "---")


def busca_nome():
    print(40 * "=")
    tigger_busca = str(input("Escreva o nome que deseja buscar:")).lower()  # Converte a entrada para minúsculas
    usuario_encontrado = False  # Variável para controlar se o nome foi encontrado

    # Itera sobre a lista de usuários
    for dicionario in lista_dados_usuarios:
        for dict_nome in dicionario.values():
            if str(dict_nome).lower() == tigger_busca:
                print("Usuário encontrado")
                usuario_encontrado = True
                break  # Sai do loop assim que encontrar o nome
        if usuario_encontrado:
            break  # Sai do loop externo se o nome foi encontrado


    if not usuario_encontrado:
        print("Usuário não encontrado")


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
    pass

def sair():
    """Finalizar a execucao"""
    pass

def menu_geral():
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
    while True:
        try:
            tigger = int(input("Escolha umas das Opções acima:"))
            if tigger <= 0 or tigger <= 7:
                break
            else:
                print("Escolha um numero entre 1 e 6 ")


        except ValueError:
            print(7*"-","Erro ao digitar  -_-",7*"-")
            print("Desculpe ! Letras,Simbolos e Numeros Reais nao são aceitos na operação")
            print("----------------------------------------------------------")
            print(5*"->","Tente Novamente!",5*"<-")


    if tigger == 1:
        print("Adicionar Usuario")
        print(40*"=")
        adicionar_usuario()
        while True:
            print('[1] - CADASTRAR UM NOVO USUARIO:'  
                  '[0] - VOLTAR:')
            continuar_cadastrando = int(input("Escolha uma das opções:"))
            if continuar_cadastrando == 1:
                adicionar_usuario()
            elif continuar_cadastrando == 0:
                menu_geral()


    elif tigger == 2:
        print("Listar Usuario")
        print(40*"=")
        while True:
            print('[1] Listar usuarios cadastrados:'
                  '[2] Buscar usuario por nome:'
                  '[0] Voltar:')
            continuar_buscando = int(input("Escolha uma das opcoes:"))
            if continuar_buscando == 1:
                listar_usuario()
            elif continuar_buscando == 2:
                busca_nome()
            elif continuar_buscando == 0:
                menu_geral()




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

def trata_int(ints):
    while True:
        try:
            # Solicitando e validando a idade do usuário
            entrada = int(ints)
            if entrada < 0:
                print("Somente numeros positivos sao aceitos")
                ints = input("Por favor, insira novamente a idade: ")  # Pede uma nova entrada
                continue  # Reinicia o loop com a nova entrada
            return entrada
        except ValueError:
            print(20 * "-", "Por favor, tente novamente!", 20 * "-")
            ints = input("Idade inválida. Por favor, insira um número válido: ")  # Solicita nova entrada


def trata_strs(strs):
    while True:
        try:
            nome = strs.strip()  # Remove espaços em branco antes e depois do nome
            if not nome.isalpha() or nome == "":  # Verifica se o nome contém apenas letras e não está vazio
                raise ValueError("Nome inválido. Números e espaços não são permitidos.")
            return nome  # Retorna o nome validado
        except ValueError as e:
            print(20 * "-", "Tente novamente!", 20 * "-")
            print(e)  # Exibe a mensagem de erro gerada
            strs = input("Nome inválido. Por favor, insira um nome: ")  # Solicita nova entrada
            return strs2






#------------------------------------------------------ Body Code-----------------------------------------------------------------------------

#------------------------------------------------------ O CODIGO COMECA A SER EXECUTADO DESTE BLOCO

menu_geral()








