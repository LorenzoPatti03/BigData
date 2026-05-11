import sys

last_word = None
tot_counter = 0

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t')
    count = int(count)
    
    if last_word and last_word != word:
        print(last_word, tot_counter, sep='\t')
        last_word = word
        tot_counter = count
    else:
        tot_counter += count
        last_word = word

if last_word:
    print(last_word, tot_counter, sep='\t')