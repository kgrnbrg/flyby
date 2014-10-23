import random
import nltk
from sys import argv
from nltk.probability import LidstoneProbDist
from nltk.stem.snowball import SnowballStemmer

script, book, do = argv

f = open(book)
t = f.read()
w = nltk.word_tokenize(t)

x = do.split('_')

estimator = lambda fdist, bins: LidstoneProbDist(fdist, 0.2)
content_model = nltk.NgramModel(3, w, estimator=estimator)

content = content_model.generate(100, x)
pos = nltk.pos_tag(content)

verbs = []

for (x, y) in pos:
	if y in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
		verbs.append(x)
	else:
		pass

st = SnowballStemmer("english")

print "You %s." % st.stem(random.choice(verbs))

