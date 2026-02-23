from Gabriele.main import Admin

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
            
    def modifica_studenti():
        pass
    def stampa_aula():
        pass
    
    
def carica_utenti_da_txt(nome_file="utenti.txt"):
    lista_caricata = []
    try:
        with open(nome_file, "r") as f:
            for riga in f:
                dati = riga.strip().split(",")
                if len(dati) == 2:
                    user, psw = dati
                    if user == "mirko" and psw == "123":
                        lista_caricata.append(Admin())
                    else:
                        lista_caricata.append(Utente(user, psw))
                        
    except FileNotFoundError:
        print(f"ERROE: File {nome_file} non trovato. Admin temporaneo per il login.")
        lista_caricata.append(Admin())
    
    print(f"DEBUG: {lista_caricata}")
    if len(lista_caricata) <=0:
        lista_caricata.append(Admin())
    return lista_caricata
    
def login(lista_utenti):
    u_in = input("Username: ")
    p_in = input("Password: ")
    
    for u in lista_utenti:
        if u.get_username() == u_in and u.get_password() == p_in:
            print("Login effettuato!")
            return u
    
    print("Credenziali fallite.")
    return None

    
dbUsers = carica_utenti_da_txt()
currentUser = login(dbUsers)