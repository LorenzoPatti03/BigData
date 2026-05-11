import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')
    
    # Gli hashtag sono il sesto campo, e sono separati tra loro da punto e virgola
    hashtags_string = fields[5]
    hashtags = hashtags_string.split(';')
    
    hashtags = [hashtag.lower() for hashtag in hashtags]
    
    for hashtag in hashtags:
        print(hashtag, 1, sep='\t')