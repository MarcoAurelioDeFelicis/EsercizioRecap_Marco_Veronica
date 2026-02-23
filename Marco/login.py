from Gabriele.utenti import Admin, Utente
    
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

    
