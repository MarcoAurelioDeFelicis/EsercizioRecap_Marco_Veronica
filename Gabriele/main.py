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


from Veronica.main import Utente

class Admin(Utente):
    def __init__(self):
        super().__init__("mirko", "123")

    
    
    
    
    def reset(self, motivazione:str):
        
        with open("studenti.csv","w") as f:
            f.write("Nome,Corso\n")

        with  open("intervento_admin.txt","a") as s:
            s.write(f"intervento:   {motivazione}\n")
        
        return f"sistema resettato con log"
    
    
    
    
    
