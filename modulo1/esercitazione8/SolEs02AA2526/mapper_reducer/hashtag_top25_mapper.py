import sys
import heapq

# heap che tiene massimo 25 elementi
top25_heap = []

for line in sys.stdin:
    line = line.strip().split('\t')
    key = line[0]
    value = int(line[1])

    # inserisce nel heap
    heapq.heappush(top25_heap, (value, key))

    # se superiamo 25 elementi, rimuoviamo il più piccolo
    if len(top25_heap) > 25:
        heapq.heappop(top25_heap)

# Ora top25_heap contiene i 25 valori più alti, ma in ordine minore -> maggiore
# Ordiniamo decrescente per stampare
top25 = sorted(top25_heap, reverse=True)

for value, key in top25:
    print(key, value, sep='\t')
