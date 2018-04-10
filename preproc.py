import operator, re, json
from words import *
from collections import Counter

f = open('lorem.txt')
text = f.read().lower()
text = re.compile(r'[^a-zA-Z]+', re.UNICODE).split(text)

stopwords = open('stop_words.txt').read()
text = [w for w in text if w not in stopwords]
text = filter(None, text)

freq = Counter(text) # magic...

data = []
for k, v in freq.most_common():
	word = Word(k, v)
	data.append(word)

with open('data.json', 'w') as out:
	json.dump([o.dump() for o in data[:70]], out, indent=4)