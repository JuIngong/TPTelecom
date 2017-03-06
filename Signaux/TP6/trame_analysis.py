'''
Created on 19 avr. 2016
@author: menez

Attention ce code est une horreur :-)
Il n'a qu'une vertu vous montrer comment analyser
les enregistrements trames Ethernet .

N'oubliez qu'il y a un aspect "art" dans la programmation
et qu'au dela du resultat fonctionnel, la structure compte tout autant !!

'''
import socket
from struct import *
import binascii


def myhexlify(a, sep=':'):
    '''
    Convert an array of bytes into a string of characters

    @param : On peut choisir un separateur entre les octets.

    @return : une string contenant la valeur hexa de chaque
    caracteres de a.

    si a[i] == 65 alors b="\x41" (code ascii du A majuscule)
    '''

    b = ("%.2x" % (a[0]))
    for c in a[1:]:
        b = b + sep + ("%.2x" % ((c)))

    return b


def manipulation_binascii():
    """
    Jouons juste ce qu'il faut avec les octets ...
    """

    """ La fonction ord() """
    c = 'A'
    v = ord(c)  # code ascii de c = i.e representation binaire de c
    print("{} = 0x{:x}".format(v, v))

    """  Definition classique d'une string  """
    s = "ff00"  # un tableau de 4 octets formant une string de 4 caracteres
    print(type(s))
    print(s)
    print("{} / {} / {} / {}".format(s[0], s[1], s[2], s[3]))
    print("{:x} / {:x} / {:x} / {:x}".format(ord(s[0]), ord(s[1]), ord(s[2]), ord(s[3])))

    """ s represente une valeur hexa  : on voudrait recuperer cette valeur """
    # => il faut un tableau de 2 octets (on rappelle qu'un octet c'est deux chiffres hexa).
    # => donc on voudrait former deux octets [FF] et [00]

    ba = binascii.unhexlify(s)
    print(type(ba))  # ba est un string de donnees binaires :
    print("{:d} / {:d}".format(ba[0], ba[1]))
    print("{:02x} / {:02x}".format(ba[0], ba[1]))

    """ En sens inverse """
    s = binascii.hexlify(ba)
    print(type(s))
    print(s)

    ba = b'\xFF\x00'  #
    print(type(ba))  # ba est une string de donnees binaires :
    print(ba)  # ca affiche les caracteres de code ASCII 'FF' et '00'
    s = binascii.hexlify(ba)
    print(type(s))  # s est une string de caracteres
    print(s)


def readtrames(filename):
    """
    Cette fonction fabrique une liste de chaines de caracteres a partir du
    fichier contenant les trames.

    Chaque chaine de la liste est une trame du fichier.

    return : liste des trames contenues dans le fichier
    """
    file = open(filename)
    trames = []

    trame = ""
    i = 1
    for line in file:  # acces au fichier ligne par ligne
        line = line.rstrip('\n')  # on enleve le retour chariot de la ligne
        line = line[6:53]  # on ne garde que les colonnes interessantes
        print("l {} : {}".format(i, line))

        if (len(line) == 0):  # print "Ligne vide :", (len(line))
            trames.append(trame.replace(' ', ''))
            trame = ""
        else:
            trame = trame + line  # .rstrip(' ') + ' '

        i = i + 1

    return trames


def type_protocole(type):
    return {
        '0800': "IPv4",
        '86DD': "IPv6",
        '0806': "ARP",
        '8035': "RARP",
        '809B': "Apple Talk",
        '88CD': "SERCOS III",
        '0600': "XNS",
        '8100': "VLAN",
    }.get(type, "Undefined")


def proto(type):
    return {
        '06': "TCP",
        '17': "UDP",
        '01': "ICMP",
    }.get(type, "Undefined")


def build_ipv4(data):
    s = ""
    s += str(int(myhexlify(data[0:1]), 16))
    s += "."
    s += str(int(myhexlify(data[1:2]), 16))
    s += "."
    s += str(int(myhexlify(data[2:3]), 16))
    s += "."
    s += str(int(myhexlify(data[3:4]), 16))
    return s


def analyse(data, protocole):  # print du contenu d'une requete
    if protocole == "ARP":  # traitement arp
        if myhexlify(data[1:2]) == '01':
            print("Type de materiel : Ethernet")
        if myhexlify(data[2:4], "") == '0800':
            print("Type protocole : IP")
        if myhexlify(data[4:5]) == '06':
            print("Longueur adresse physique : Ethernet")
        if myhexlify(data[5:6]) == '04':
            print("Longueur adresse logique : IPv4")
        if myhexlify(data[5:6]) == '06':
            print("Longueur adresse logique : IPv6")
        if myhexlify(data[7:8]) == '01':
            print("Operation : Request")
        if myhexlify(data[7:8]) == '02':
            print("Operation : Reply")
        print("Adresse mac source : {}".format(myhexlify(data[8:14])))
        print("Adresse IP source : {}".format(build_ipv4(data[14:18])))
        print("Adresse mac destination : {}".format(myhexlify(data[18:24])))  # vide dans le cas d'une requete
        print("Adresse IP destination : {}".format(build_ipv4(data[24:28])))
    elif protocole == "IPv4":  # traitement ipv4
        d = myhexlify(data, "")
        print("Version Ip : " + d[0:1])
        print("Longueur entete : " + d[1:2])
        print("Longueur : " + str(int(d[4:8], 16)))
        print("Duree de vie : " + str(int(d[16:18], 16)))

        p = proto(d[18:20])
        print("Protocole : " + p)
        print("Adresse source : {}.{}.{}.{}".format(int(d[20:22], 16), int(d[22:24], 16), int(d[24:26], 16),
                                                    int(d[26:28], 16)))
        print("Adresse dest : {}.{}.{}.{}".format(int(d[28:30], 16), int(d[30:32], 16), int(d[32:34], 16),
                                                  int(d[34:36], 16)))


def decodageEthernet(trame):
    """
    Analyse une trame Ethernet :
    cf https://fr.wikipedia.org/wiki/Ethernet
    Input : trame est une chaine de caracteres
    """
    print("\n\nTrame Ethernet :\n"), trame  # Un chaine de caracteres
    trame = binascii.unhexlify(trame)  # Les octets representes par cette chaine

    print("Header Ethernet :")  # parse ethernet header
    eth_length = 14
    eth_header = trame[:eth_length]
    eth_data = trame[eth_length:]
    print(type(eth_header))

    # Parsing de l'entete Ethernet en utilisant le slicing Python
    print('Destination MAC : {}'.format(myhexlify(eth_header[0:6])))
    print('Source MAC : {}'.format(myhexlify(eth_header[6:12])))
    # On enregistre le type de protocole
    prot = type_protocole(myhexlify(eth_header[12:14], ""))
    print('Type de protocole : {}'.format(prot))

    print('\nData : ')
    # On print ce qui est dans les donnée
    analyse(eth_data, prot)


# =================================================================

if __name__ == '__main__':

    # Pour comprendre les manipulations de bytes :
    manipulation_binascii()

    # Transformation des echanges contenus dans le fichier
    # vers une liste de strings
    trames = readtrames("XXXgr1.txt")
    # print(trames)

    # Analyse de chaque trame de la liste
    for trame in trames:
        decodageEthernet(trame)
