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


def criptografar(x):
    """Função para criptografar"""
    chave1Publica,chave2Publica= lerChaves("chavePublica")
    y = ord(x)**chave1Publica%chave2Publica
    return y


def descriptografar(y):
    """Função para descriptografar"""
    chave1Privada,chave2Privada=lerChaves("chavePrivada")
    x = chr(int(y)**chave1Privada%chave2Privada)
    return x


def lerChaves(caminho):
    """Função para ler as chaves"""
    arq=open(caminho+".txt","r")
    lista=[]
    string = ""
    for caractere in arq.read():
        if caractere!=" ":
            string+=caractere
        else:
            lista.append(int(string))
            string=""
    lista.append(int(string))
    arq.close()
    return lista[0],lista[1]
