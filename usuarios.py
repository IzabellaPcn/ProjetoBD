"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF968 - Programação 1

Autora: Izabella Priscylla da Costa Nascimento (ipcn)
Email: ipcn@cin.ufpe.br
Data: 22-05-2018
Copyright(c) 2018 Izabella Priscylla da Costa Nascimento
"""


from criptografia import criptografar, descriptografar
from log import log, buscarLog


def lerUsuario():
    """Função para ler o usuário do arquivo e retorna o dicionário contento o cadastros dos usuários,
     com senha e nível do usuário"""
    arq = open("usuarios.txt", "r")
    lista = []
    dicionario = {}
    adicionar = ""
    texto = arq.read()
    adicionar2 = ""
    texto2 = ""
    for caractere in texto:
        if caractere != " ":
            adicionar2 += caractere
        else:
            texto2 += descriptografar(adicionar2)
            adicionar2 = ""
    for linha in texto2.split('\n'):
        adicionar = ""
        lista = []
        for elemento in linha:
            if (elemento != ";")and (elemento != "\n"):
                adicionar += elemento
            else:
                lista.append(adicionar)
                adicionar = ""
        if lista:
            lista.append(adicionar)
            dicionario[lista[0]] = (lista[1], lista[2])
        lista = []
    arq.close()
    print(dicionario)
    return(dicionario)


def gravarUsuarioArquivo(dicionario):
    """Função para gravar o dicionario no arquivo"""
    arq = open("usuarios.txt", "w")
    string = ""
    for x in dicionario:
        string += x + ";" + dicionario[x][0] + ";" + dicionario[x][1] + "\n"
    stringNova = ""
    for caractere in string:
        stringNova += str(criptografar(caractere)) + " "
    arq.write(stringNova)
    arq.close()


def nivelUsuario():
    """Funçao para adicionar o nível do usuário"""
    nivel = int(input("1 - Bibliotecário\n"
                      "2 - Atendente\n"
                      "3 - Visitante "))
    print("")
    if (nivel == 1):
        nivel = "Bibliotecário"
    elif (nivel == 2):
        nivel = "Atendente"
    elif (nivel == 3):
        nivel = "Visitante"
    else:
        print("Opção não encontrada, digite novamente.\n")
        print("Para qual nível deseja modificar?")
        return nivelUsuario()
    return nivel


def buscarNivelUsuario(bancoDeDados, usuario):
    """Função para buscar o nível do usuário"""
    nivel = bancoDeDados[usuario][1]
    return nivel


def modificarNivelUsuario(bancoDeDados):
    """Função para modificar o nível do usuário"""
    print("")
    continuar = False
    while continuar == False:
        print("Usuários cadastrados:")
        listarNivelUsuarios(bancoDeDados)
        usuario = input("\nQual usuário deseja modificar? ")
        print("")
        if usuario == "adm":
            print("Não é possível modificar o nível deste usuário.\n")
        else:
            print("Para qual nível deseja modificar?")
            nivelAntigo = bancoDeDados[usuario][1]
            bancoDeDados[usuario] = (bancoDeDados[usuario][0], nivelUsuario())
            log(usuario, "modificou_nível_de_usuário")
            print("Nível do usuário '", usuario, "' modificado de ",
                nivelAntigo, " para ", bancoDeDados[usuario][1], ".\n")
            return bancoDeDados


def listarUsuarios(bancoDeDados):
    for chave in bancoDeDados.keys():
        print(chave)


def listarNivelUsuarios(bancoDeDados):
    for pares in bancoDeDados.items():
        print(pares[0], "-", pares[1][1])


def adicionarUsuario(bancoDeDados, usuario):
    """Função para adicionar um novo usuário do bando de dados"""
    login = input("\nDigite o login do usuário a ser adicionado: ")
    achou = False
    for x in bancoDeDados:
        if login == x:
            achou = True
    if achou == False:
        senha = input("Digite a senha: ")
        print("")
        bancoDeDados[login] = (senha, "Visitante")
        log(usuario, "adicionou_usuário")
        print("Usuário '", login, "' adicionado com sucesso.\n")
    else:
        print("\nLogin já cadastrado.\n")
    return bancoDeDados


def removerUsuario(bancoDeDados, usuario):
    """Função para remover um usuário do bando de dados"""
    print("")
    continuar = False
    while continuar == False:
        print("Qual usuário deseja remover?")
        listarUsuarios(bancoDeDados)
        login = input("\nDigite o login do usuário: ")
        print("")
        if login == "adm":
            print("Não é possível remover este usuário.\n")
        elif login in bancoDeDados:
            bancoDeDados.pop(login)
            log(usuario, "removeu_usuário")
            print("Usuário removido com sucesso.\n")
            return bancoDeDados
        else:
            print("Usuário não consta no sistema.\n")
