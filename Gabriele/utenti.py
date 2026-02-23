
'''Esercizio Recap
Obiettivo
Verificare la comprensione della gestione dei file in Python applicando le tre regole fondamentali:
Gestire la modalità di apertura (r, w, a)

Recap delle tre regole fondamentali

Realizza un programma Python che gestisca un file chiamato studenti.txt e svolga le seguenti operazioni:

Crea un sistema ripetitivo che permetta di: registrarsi, fare login.

Chieda all’utente per registrarsi di inserire nome e password.

Salvi i nomi nel file credenziali.txt, uno per riga.

Quando un utente è loggato può fare due cose: Ins.Mod studenti o Stampare l’aula.

In Ins.Mod. studenti devo poter aggiungere uno studente (atr: Nome, CORSO) o modificarne la lista in file csv.

Stampa la lista deve stampare tutta l’aula ordinando gli studenti per corso.

Creare una classe figlia di utente che è admin che può ressetare completamente la lista e non deve registrarsi ma solo accedere perché è hardcodato dentro il sistema; rimane un file txt chiamato intervento utente con la motivazione.'''
import pandas as pd

class Utente:
    def __init__(self, username:str, password:str):
        self.__username = username
        self.__password = password
        
    # --- GETTER ---
    def get_username(self):
        return self.__username
    
    def get_password(self):
        return self.__password

    # --- SETTER ---
    def set_password(self, nuova_pass):
        if len(nuova_pass) > 3:
            self.__password = nuova_pass
        else:
            print("Password troppo corta!")
            
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




class Admin(Utente):
    def __init__(self):
        super().__init__("mirko", "123")
    
    def reset(self, motivazione:str):
        try:
            with open("studenti.csv","w") as f:
                f.write("Nome,Corso\n")

            with  open("intervento_admin.txt","a") as s:
                s.write(f"intervento:   {motivazione}\n")
            
            return f"sistema resettato con log"
        except PermissionError:
            return "Errore: Permesso negato. Chiudi i file se sono aperti in Excel!"
        except IOError as e:
            return f"Errore di sistema durante la scrittura: {e}"
        except Exception as e:
            return f"Si è verificato un errore imprevisto: {e}"
        except FileNotFoundError:
            return f"Si è verificato un errore con l'apertura: {e}"
    
    def CreUtente(self,nome:str,password:str):
        n_Utente = Utente(nome,password)
        new_user = str(nome + " , " + password)
        print(f"DEBUG: {new_user} TIPO: {type(new_user)}")
        
        try:
            with open("utenti.txt", "a") as f:
                f.write(new_user)
        except FileNotFoundError as e :
            print(f"Si è verificato un errore con l'apertura: {e}")
            with open("utenti.txt", "x") as f:
                f.write(new_user)
    
        return n_Utente
            