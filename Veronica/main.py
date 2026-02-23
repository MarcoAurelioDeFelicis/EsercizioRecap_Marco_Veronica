'''Esercizio Recap
Obiettivo
Verificare la comprensione della gestione dei file in Python applicando
le tre regole fondamentali:
Gestire la modalità di apertura (r, w, a)
Recap delle tre regole fondamentali
Realizza un programma Python che gestisca un file chiamato studenti.txt
e svolga le seguenti operazioni:
Crea un sistema ripetitivo che permetta di: registrarsi, fare login.
Chieda all’utente per registrarsi di inserire nome e password.
Salvi i nomi nel file credenziali.txt, uno per riga.
Quando un utente è loggato può fare due cose: Ins.Mod studenti o
Stampare l’aula.
In Ins.Mod. studenti devo poter aggiungere uno studente (atr: Nome, CORSO)
o modificarne la lista in file csv.
Stampa la lista deve stampare tutta l’aula ordinando gli studenti per
corso.
Creare una classe figlia di utente che è admin che può ressetare
completamente la lista e non deve registrarsi ma solo accedere perché
è hardcodato dentro il sistema; rimane un file txt chiamato intervento
utente con la motivazione.'''

class Utente:
    def __init__(self, username:str, password:str):
        self.__username = username
        self.__password = password
    
    def modifica_studenti(nome, cognome, newcorso):
        righe = []
        with open("studenti.csv", "r") as file:
            contenuto = file.read(file)
            for riga in contenuto:
                splitted_riga = riga.split(",")
                righe.append(splitted_riga)

            for riga in righe:
                if riga[0] == nome and riga[1] == cognome:
                    riga[2] = newcorso

        with open("studenti.csv", "w") as file:
            writer = file.write(righe)

    def stampa_aula():
        with open("studenti.csv", "r") as file:
            contenuto = file.read()
        print(contenuto)


class Admin(Utente):
    def __init__(self):
        super().__init__("mirko", "123")

    def reset():
        pass

class Studente:
    def __init__(self, nome:str, cognome:str, corso:str):
        self.__nome = nome
        self.__cognome = cognome
        self.__corso = corso
    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome: str):
        self.__nome = nome

    def get_cognome(self):
        return self.__cognome
    
    def set_nome(self, cognome: str):
        self.__cognome = cognome

    def get_corso(self):
        return self.__corso
    
    def set_corso(self, corso: str):
        self.__corso = corso