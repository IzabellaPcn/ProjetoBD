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


from log import log, buscarLog


def logar(bancoDeDados):
    """Função para logar"""
    continuar = False
    while continuar == False:
        login = input("Digite o login: ")
        senha = input("Digite a senha: ")
        print("")
        if login in bancoDeDados:
            if senha == bancoDeDados[login][0]:
                usuario = login
                log(usuario, "logou")
                return usuario
            else:
                print("Senha não corresponde ao usuário.\n")
        else:
            print("Login não cadastrado no banco de dados.\n")
