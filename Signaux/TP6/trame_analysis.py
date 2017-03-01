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

    b = ("%.2x" % (ord(a[0])))
    for c in a[1:]:
        b = b + sep + ("%.2x" % (ord(c)))

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
    print(type(eth_header))

    # Parsing de l'entete Ethernet en utilisant le slicing Python
    print('Destination MAC : {}'.format(myhexlify(eth_header[0:6])))
    print('Destination MAC : {}'.format(binascii.hexlify(eth_header[0:6])))

    # une autre facon d'extraire les champs de l'entete !
    # For more information on format strings and endiannes, refer to
    # https://docs.python.org/3.5/library/struct.html
    ethfields = unpack('!6s6sH', eth_header)
    adrd_mac = ethfields[0]
    adrs_mac = ethfields[1]
    print('Destination MAC : {}'.format(myhexlify(adrd_mac)))


# =================================================================

if __name__ == '__main__':

    # Pour comprendre les manipulations de bytes :
    manipulation_binascii()

    # Transformation des echanges contenus dans le fichier
    # vers une liste de strings
    trames = readtrames("XXX.txt")
    print(trames)

    # Analyse de chaque trame de la liste
    for trame in trames:
        decodageEthernet(trame)
