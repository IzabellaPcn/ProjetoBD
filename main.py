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


from datetime import datetime
from criptografia import criptografar, descriptografar
from usuarios import lerUsuario, gravarUsuarioArquivo, buscarNivelUsuario, modificarNivelUsuario, listarUsuarios, adicionarUsuario, removerUsuario
from log import log, buscarLog
from elementos import lerElemento, gravarElementoArquivo, adicionarElemento, removerElemento, buscarElemento, atualizarElemento, ordenarElementos, buscarNaTela
from login import logar


def menuNivelBibliotecario():
    """Função menu do usuário maior nível"""
    opcao = int(input("------- O que deseja fazer? -------\n"
                      "1 - Adicionar usuário\n"
                      "2 - Remover Usuário\n"
                      "3 - Modificar nível do usuário\n"
                      "4 - Adicionar livro\n"
                      "5 - Atualizar livro\n"
                      "6 - Remover livro\n"
                      "7 - Buscar livro\n"
                      "8 - Buscar nos logs\n"
                      "9 - Logout "))
    return opcao


def menuNivelAtendente():
    """Função menu do usuário de nível intermediário """
    opcao = int(input("------- O que deseja fazer? -------\n"
                      "1 - Adicionar livro\n"
                      "2 - Atualizar livro\n"
                      "3 - Buscar livro\n"
                      "4 - Logout "))
    return opcao


def menuNivelVisitante():
    """Função menu do usuário de nível visitante"""
    opcao = int(input("------- O que deseja fazer? -------\n"
                      "1 - Buscar livro\n"
                      "2 - Logout "))
    return opcao


opcao = 0
bancoDeDados = lerUsuario()
bancoDeDadosElementos = lerElemento()
continuarGeral = True


while(continuarGeral == True):
    """Laço para encerrar o programa"""
    verificar = int(input("\nO que deseja fazer? \n"
                          "1 - Login\n"
                          "2 - Sair do progama "))
    print("")
    if verificar == 1:
        usuario = logar(bancoDeDados)
        nivel = buscarNivelUsuario(bancoDeDados, usuario)
        if nivel == "Bibliotecário":
            continuar = True
            while continuar == True:
                """Laço para encerrar o nível do bibliotecário"""
                opcao = menuNivelBibliotecario()
                if opcao == 1:
                    bancoDeDados = adicionarUsuario(bancoDeDados, usuario)
                elif opcao == 2:
                    removerUsuario(bancoDeDados, usuario)
                elif opcao == 3:
                    modificarNivelUsuario(bancoDeDados)
                elif opcao == 4:
                    adicionarElemento(bancoDeDadosElementos, usuario)
                elif opcao == 5:
                    atualizarElemento(bancoDeDadosElementos, usuario)
                elif opcao == 6:
                    removerElemento(bancoDeDadosElementos, usuario)
                elif opcao == 7:
                    buscarNaTela(bancoDeDadosElementos, usuario)
                elif opcao == 8:
                    buscarLog()
                elif opcao == 9:
                    log(usuario, "deslogou")
                    continuar = False
                else:
                    print("\nOpção não encontrada, digite novamente.\n")
        elif nivel == "Atendente":
            continuar = True
            while continuar == True:
                """Laço para encerrar o nível do atendente"""
                opcao = menuNivelAtendente()
                if opcao == 1:
                    adicionarElemento(bancoDeDadosElementos, usuario)
                elif opcao == 2:
                    atualizarElemento(bancoDeDadosElementos, usuario)
                elif opcao == 3:
                    buscarNaTela(bancoDeDadosElementos, usuario)
                elif opcao == 4:
                    log(usuario, "deslogou")
                    continuar = False
                else:
                    print("\nOpção não encontrada, digite novamente.\n")
        else:
            continuar = True
            while continuar == True:
                """Laço para encerrar o nível do visitante"""
                opcao = menuNivelVisitante()
                if opcao == 1:
                    buscarNaTela(bancoDeDadosElementos, usuario)
                elif opcao == 2:
                    log(usuario, "deslogou")
                    continuar = False
                else:
                    print("\nOpção não encontrada, digite novamente.\n")
    elif verificar == 2:
        continuarGeral = False
    else:
        print("Opção não encontrada, digite novamente.")


gravarUsuarioArquivo(bancoDeDados)
gravarElementoArquivo(bancoDeDadosElementos)
ordenarElementos(bancoDeDadosElementos)
