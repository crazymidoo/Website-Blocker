import datetime  # Importo datetime per lavorare con date e orari
import time  # Importo time per gestire il tempo e ritardi

# Qui imposto la data di fine (quando i siti saranno sbloccati)
end_time = datetime.datetime(2025, 9, 1)

# Questo è il sito da bloccare
site_block = ["www.nike.com"]

# Percorso del file 'hosts' su Windows
host_path = "C:/Windows/System32/drivers/etc/hosts"

# Indirizzo IP di reindirizzamento (localhost)
redirect = "127.0.0.1"

# Ciclo che controlla se bloccare o sbloccare i siti
while True:
    # Se il tempo corrente è prima della data di fine
    if datetime.datetime.now() < end_time:
        print("Start Blocking")  # Messaggio per avvisare che i siti stanno per essere bloccati
        with open(host_path, "r+") as host_file:  # Apre il file 'hosts' in modalità lettura e scrittura
            content = host_file.read()  # Legge tutto il contenuto del file
            # Ciclo per ogni sito da bloccare
            for website in site_block:
                # Se il sito non è già presente nel file 'hosts', lo aggiungi
                if website not in content:
                    host_file.write(redirect + " " + website + "\n")  # Aggiungi il sito bloccato
    else:
        # Se il tempo è trascorso (cioè se la data di fine è arrivata)
        with open(host_path, "r+") as host_file:  # Riapre il file 'hosts' in modalità lettura e scrittura
            content = host_file.readlines()  # Legge tutte le righe del file
            host_file.seek(0)  # Torna all'inizio del file per riscrivere
            # Ciclo per controllare ogni riga del file
            for lines in content:
                # Se la riga non contiene nessun sito da bloccare, la riscrive
                if not any(website in lines for website in site_block):
                    host_file.write(lines)  # Scrive la riga nel file
            host_file.truncate() # Rimuove eventuali righe rimanenti dopo il punto in cui il file è stato riscritto

    time.sleep(5) # Pausa di 5 secondi prima di ripetere il ciclo
