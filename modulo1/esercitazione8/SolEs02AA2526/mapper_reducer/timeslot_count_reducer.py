import sys

last_timeslot = None
tot_counter = 0

for line in sys.stdin:
    
    line = line.strip()
    timeslot, count = line.split('\t')
    count = int(count)
    
    if last_timeslot and last_timeslot != timeslot:
        
        print(last_timeslot, tot_counter, sep='\t')
        last_timeslot = timeslot
        tot_counter = count
    else:
        tot_counter += count
        last_timeslot = timeslot

if last_timeslot:
    print(last_timeslot, tot_counter, sep='\t')