import datetime

def assistente_virtuale(comando):
    comando = comando.strip().lower()  
    
    if comando == "data":
        oggi = datetime.date.today()
        risposta = "La data di oggi è " + oggi.strftime("%d/%m/%Y")
    elif comando == "ora":
        ora_attuale = datetime.datetime.now().time()
        risposta = "L'ora attuale è " + ora_attuale.strftime("%H:%M")
    elif comando == "nome":
        risposta = "Mi chiamo Assistente Virtuale"
    else:
        risposta = "Non ho capito la tua domanda."
    
    return risposta

while True:
    comando_utente = input("Cosa vuoi sapere?\n(Ora, Data, Nome) or 'esci' to quit: ")
    if comando_utente.strip().lower() == "esci":
        print("Arrivederci!")
        break
    else:
        print(assistente_virtuale(comando_utente))

