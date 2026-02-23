from Marco.login import login, carica_utenti_da_txt
from Gabriele.utenti import Admin , Utente



def play():
    dbUsers = carica_utenti_da_txt()
    currentUser = login(dbUsers)
    
    if currentUser:
        print(f"\n--- Benvenuto: {currentUser.get_username()} ---")
        azioni_disponibili = {"1": "Visualizza Aula"}
                
        if isinstance(currentUser, Admin):
                                                #unire |= o .update()
            azioni_disponibili.update({
                "2": "Crea Alunno (CSV)", 
                "3": "Reset"
            })
        else:
            azioni_disponibili.update({
                "4": "Modifica Studenti"
            })
        
        while True: 
            
            print(f"\nAzione disponibili:")
            for tasto, azione in azioni_disponibili.items():
                print(f"[{tasto}] {azione}")
                
            scelta = input("\nScegli il numero dell'azione (o '0' per uscire): ")
            
            if scelta == "0":
                print("Arrivederci!")
                break
            
            elif scelta in azioni_disponibili:
                if scelta == "1":
                    if not currentUser.stampa_aula:
                        print("ERRORE")
                    pass
                
                elif scelta == "2":
                    new_username = input("inserisci il nuovo username")
                    new_password = input("inserisci nuova password")
                    
                    currentUser.CreUtente(new_username, new_password)
                    
                    if not currentUser:
                        print( "ERRORE: creazione non andata a buoin fine ")
                        
            else:
                print("Scelta non valida.")
            
    else:
        print("Login fallito. Programma terminato.")




if __name__ == "__main__":
    play()
    
        
        
    
