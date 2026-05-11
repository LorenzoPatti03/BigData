import sys
from datetime import datetime, time

# Definizione degli slot
mattina_to_pomeriggio = time(6,0,0)       # 06:00 - 15:00
pomeriggio_to_sera = time(15,0,0)         # 15:00 - 20:00
sera_to_notte = time(20,0,0)              # 20:00 - 00:00
notte_to_mattina = time(0,0,0)            # 00:00 - 06:00

for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')
    
    tweet_id = fields[0]
    time_str = fields[4].split(' ')[1]  # es. "14:35:22"
    
    t = datetime.strptime(time_str, "%H:%M:%S").time()  # solo orario

    if mattina_to_pomeriggio <= t < pomeriggio_to_sera:
        print('pomeriggio', 1, sep='\t')
    elif pomeriggio_to_sera <= t < sera_to_notte:
        print('sera', 1, sep='\t')
    elif sera_to_notte <= t or t < notte_to_mattina:  # gestisce la mezzanotte
        print('notte', 1, sep='\t')
    elif notte_to_mattina <= t < mattina_to_pomeriggio:
        print('mattina', 1, sep='\t')
