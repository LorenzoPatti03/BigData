import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')
    
    date, time = fields[4].split()
    hour, minute, second = time.split(':')
    hour = int(hour)
    
    if hour >= 6 and hour <= 14:
        print('Mattina', 1, sep='\t')
    elif hour <= 19:
        print('Pomeriggio', 1, sep='\t')
    else:
        print('Sera e notte', 1, sep='\t')