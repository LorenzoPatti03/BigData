import sys

top_hashtags = list()
k = 25

for line in sys.stdin:
    line = line.strip()
    hashtag, count = line.split('\t')
    count = int(count)
    
    value = (count, hashtag)    
    
    if len(top_hashtags) < k:
        top_hashtags.append(value)
    elif value > top_hashtags[0]:
        top_hashtags[0] = value
    
    top_hashtags.sort()
    
for count, hashtag in top_hashtags[::-1]:
    print(hashtag, count, sep='\t')