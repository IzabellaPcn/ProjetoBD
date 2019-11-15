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
from usuarios import lerUsuario, gravarUsuarioArquivo, buscarNivelUsuario, modificarNivelUsuario, listarUsuarios


def lerElemento():
    """Função para ler os elementos e retorna o dicionário contento o cadastros dos elementos com ISBN, título, autor,
    número de chamada, edição,acervo, ano de publicação"""
    arq = open("elementos.txt", "r")
    lista = []
    dicionarioElementos = {}
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
        for elemento in linha:
            if (elemento != ";")and (elemento != "\n"):
                adicionar += elemento
            else:
                lista.append(adicionar)
                adicionar = ""
        if lista:
            lista.append(adicionar)
            dicionarioElementos[lista[0]] = (
                lista[1], lista[2], lista[3], lista[4], lista[5], lista[6])
        lista = []
    arq.close()
    print(dicionarioElementos)
    return(dicionarioElementos)


def gravarElementoArquivo(dicionarioElementos):
    """Função para gravar o dicionario dos elementos no arquivo"""
    arq = open("elementos.txt", "w")
    string = ""
    for x in dicionarioElementos:
        string += x + ";" + dicionarioElementos[x][0] + ";" + dicionarioElementos[x][1] + ";" + \
            dicionarioElementos[x][2] + ";" + dicionarioElementos[x][3] + ";" + \
            dicionarioElementos[x][4] + ";" + dicionarioElementos[x][5] + "\n"
    stringNova = ""
    for caractere in string:
        stringNova += str(criptografar(caractere)) + " "
    arq.write(stringNova)
    arq.close()


def adicionarElemento(bancoDeDadosElementos, usuario):
    """Função para adicionar livros"""
    ISBN = input("\nDigite o ISBN: ")
    achou = False
    for x in bancoDeDadosElementos:
        if ISBN == x:
            achou = True
    if achou == False:
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        numeroDeChamada = input("Digite o número de chamada do livro: ")
        edicao = input("Digite a edição do livro: ")
        acervo = input("Digite o acervo do livro: ")
        anoDePublicacao = input("Digite o ano de publicação do livro: ")
        print("")
        bancoDeDadosElementos[ISBN] = (
            titulo, autor, numeroDeChamada, edicao, acervo, anoDePublicacao)
        log(usuario, "adicionou_elemento")
        print("Livro adicionadao com sucesso.\n")
    else:
        print("\nISBN já cadastrado.\n")
    return bancoDeDadosElementos


def removerElemento(bancoDeDadosElementos, usuario):
    """Função para remover livro"""
    print("")
    print("Qual livro deseja remover?\n")
    listarElemento(bancoDeDadosElementos, 4)
    ISBN = input("\nDigite o ISBN: ")
    print("")
    if ISBN in bancoDeDadosElementos:
        bancoDeDadosElementos.pop(ISBN)
        log(usuario, "removeu_elemento")
        print("Livro removido com sucesso.\n")
    else:
        print("Livro não cadastrado no sistema.\n")
    return bancoDeDadosElementos


def listarElemento(bancoDeDadosElementos, opcaoListar):
    if opcaoListar == 1:
        for chave in bancoDeDadosElementos.keys():
            print("ISBN: ", chave)
    elif opcaoListar == 2:
        for chave in bancoDeDadosElementos.keys():
            print("Título: ", bancoDeDadosElementos[chave][0])
    elif opcaoListar == 3:
        for chave in bancoDeDadosElementos.keys():
            print("Autor: ", bancoDeDadosElementos[chave][1])
    else:
        for chave in bancoDeDadosElementos.keys():
            print("ISBN: ", chave, ", Título: ",
                  bancoDeDadosElementos[chave][0])


def buscarElemento(bancoDeDadosElementos):
    """Função buscar livro"""
    opcao = int(input("\nComo deseja buscar o livro?\n"
                      "1 - ISBN\n"
                      "2 - Título\n"
                      "3 - Autor "))
    print("")
    if opcao == 1:
        listarElemento(bancoDeDadosElementos, 1)
        ISBN = input("\nDigite o ISBN: ")
        if ISBN in bancoDeDadosElementos:
            return ISBN
        else:
            return False
    elif opcao == 2:
        listarElemento(bancoDeDadosElementos, 2)
        titulo = input("\nDigite o título: ")
        for atributo in bancoDeDadosElementos.items():
            if atributo[1][0] == titulo:
                return atributo[0]
        return False
    elif opcao == 3:
        listarElemento(bancoDeDadosElementos, 3)
        autor = input("\nDigite o autor: ")
        for atributo in bancoDeDadosElementos.items():
            if atributo[1][1] == autor:
                return atributo[0]
        return False
    else:
        print("Opção não encontrada, digite novamente.")
        buscarElemento(bancoDeDadosElementos)


def atualizarElemento(bancoDeDadosElementos, usuario):
    """Função para atualizar os livros"""
    opcao = buscarElemento(bancoDeDadosElementos)
    if opcao == False:
        print("\nElemento não cadastrado no sistema.\n")
    else:
        atualizar = int(input("\n------- O que deseja atualizar? ------\n"
                              "1 - Título\n"
                              "2 - Autor\n"
                              "3 - Número de chamada\n"
                              "4 - Edição\n"
                              "5 - Acervo\n"
                              "6 - Ano de Publicação "))
        if (atualizar < 1)or(atualizar > 6):
            print("\nOpção não encontrada, digite novamente.")
            return atualizarElemento(bancoDeDadosElementos, usuario)
        elementosDaChave = list(bancoDeDadosElementos[opcao])
        elementosDaChave[atualizar-1] = input("\nDigite o novo atributo: ")
        print("\nLivro atualizado com sucesso.\n")
        bancoDeDadosElementos[opcao] = tuple(elementosDaChave)
        log(usuario, "atualizou_elemento")
    return bancoDeDadosElementos


def ordenarElementos(bancoDeDadosElementos):
    """Função para ordenar os elementos"""
    lista = []
    for chave in bancoDeDadosElementos:
        lista.append(int(chave))
    ordenado = sorted(lista)
    arq = open("impressaoelementos.txt", "w")
    for x in ordenado:
        arq.write("ISBN: " + str(x) + ", Título: " + bancoDeDadosElementos[str(x)][0] + ", Autor: "
                  + bancoDeDadosElementos[str(x)][1] + ", Número de chamada: " +
                  bancoDeDadosElementos[str(x)][2] + ", Edição: "
                  + bancoDeDadosElementos[str(x)][3]+", Acervo: " +
                  bancoDeDadosElementos[str(x)][4]+", Ano de Publicação:"
                  + bancoDeDadosElementos[str(x)][5])
        arq.write("\n")
    arq.close()


def buscarNaTela(bancoDeDadosElementos, usuario):
    """Função para imprimir na tela a busca do elemento"""
    ISBN = buscarElemento(bancoDeDadosElementos)
    if (ISBN != False):
        print("\nISBN: " + ISBN + "\nTítulo: " + bancoDeDadosElementos[ISBN][0] + "\nAutor: " + \
        bancoDeDadosElementos[ISBN][1] + "\nNúmero de chamada: " + bancoDeDadosElementos[ISBN][2] + \
        "\nEdição: " + bancoDeDadosElementos[ISBN][3] + "\nAcervo: " + bancoDeDadosElementos[ISBN][4] + \
        "\nAno de publicação: " + bancoDeDadosElementos[ISBN][5])
        print("")
        log(usuario, "buscou_elemento")
    else:
        print("\nLivro não cadastrado no sistema.\n")
