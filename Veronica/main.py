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

import pandas as pd



class Utente:
    def __init__(self, username:str, password:str):
        self.__username = username
        self.__password = password
    
    def modifica_studenti(self,nome, cognome, newcorso):
        righe = []
        with open("studenti.csv", "r") as file:
            contenuto = file.read(file)
            for riga in contenuto:
                splitted_riga = riga.strip().split(",")
                righe.append(splitted_riga)

            for riga in righe[1:]:
                if riga[0] == nome and riga[1] == cognome:
                    riga[2] = newcorso
                    break

        with open("studenti.csv", "w") as file:
            writer = file.write(righe)

    def stampa_ordinata(self, file):
        try:
            pf = pd.read_csv(file)
            pf_ordinato = pf.sort_values(by= "Corso")
            lista_utenti = pf_ordinato.to_dict(orient="records")
            for utenti in lista_utenti:
                print(f"Nome {utenti["Nome"]} Cognome {utenti["Cognome"]} Corso {utenti["Corso"]}")
            return lista_utenti
        except FileNotFoundError as e:
            print(f"Errore {e}")
            return None
        except Exception as e:
            print(f"Si è verificato un errore {e}")
            return None

    def stampa_aula(self, file):
        studenti = []
        with open(file, "r") as file:
            contenuto = file.read(file)
            for riga in contenuto:
                splitted_riga = riga.strip().split(",")
                studenti.append(splitted_riga)
        lista_ordinata = self.stampa_ordinata(file)
        return lista_ordinata


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