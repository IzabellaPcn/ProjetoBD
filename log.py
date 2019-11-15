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


def log(usuario, acao):
    """Função log"""
    arq = open("log.txt", "a")
    tempo = datetime.today()
    dia = str(tempo.day)
    mes = str(tempo.month)
    if len(dia) == 1:
        dia = "0" + dia
    if len(mes) == 1:
        mes = "0" + mes
    arq.write(usuario + " " + acao + " em " + dia+"-"+mes+"-"+str(tempo.year) + " as "
              + str(tempo.hour) + ":" + str(tempo.minute) + ":" + str(tempo.second)+"\n")
    arq.close()


def tipoBuscaLog():
    """Função para saber qual parâmetro buscar o log"""
    opcao = int(input("\nComo deseja buscar o log?\n"
                      "1 - Data de execução\n"
                      "2 - Usuário "))
    if opcao == 1:
        data = input("\nDidite a data: (dd-mm-aaaa)")
        print("")
        return data
    elif opcao == 2:
        usuario = input("\nDigite o usuário: ")
        print("")
        return usuario
    else:
        print("\nOpção não encontrada, digite novamente.")
        return tipoBuscaLog()


def buscarLog():
    """Função para buscar o log"""
    arq = open("log.txt", "r")
    lista = []
    adicionar = ""
    opcao = tipoBuscaLog()
    for string in arq.readlines():
        for caractere in string:
            if (caractere != " ") and (caractere != "\n"):
                adicionar += caractere
            else:
                lista.append(adicionar)
                adicionar = ""
        if opcao == lista[3]:
            print("" + lista[0] + " " + lista[1] + " " + lista[2] +
                  " " + lista[3] + " " + lista[4] + " " + lista[5])
        elif opcao == lista[0]:
            print("" + lista[0] + " "+lista[1] + " " + lista[2] +
                  " " + lista[3] + " " + lista[4] + " " + lista[5])
        lista = []
    print("")
    arq.close()
