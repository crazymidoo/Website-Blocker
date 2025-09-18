# Website Blocker 

Uno script Python semplice per bloccare i siti che ti distraggono fino a quando decidi tu di sbloccarli!

## Come funziona
 
- Blocca i siti web che scegli modificando il file `hosts`.- Mantiene il blocco fino a una data che imposti.  
- Quando arriva la data, sblocca automaticamente i siti.  
- Controlla ogni 5 secondi se deve bloccare o sbloccare.

## Perchè usarlo?

- Aiuta a rimanere concentrato ed evitare distrazioni.

- Utile per studio, lavoro o quando vuoi avere più autocontrollo online.  

- Molto semplice da configurare e immediato da usare.

## Come usarlo 

Esegui il file come amministratore, apri lo script e modifica le impostazioni:  

```python
site_block = ["www.nike.com"]          # siti da bloccare
end_time = datetime.datetime(2025, 9, 1)  # data di fine blocco

# Puoi aggiungere più siti da bloccare all'interno della lista site_block, ad esempio:
site_block = ["www.nike.com", "www.youtube.com", "www.instagram.com"]



