
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import re


f = open('big.txt')
s = f.read().lower()

exclude = string.punctuation
m=re.split("[" + exclude + "]+", s)
sx = ' '.join(m)


stop_words = set(stopwords.words('english'))
tokens = word_tokenize(sx)

ss = [ch for ch in tokens if not ch in stop_words]


lemmatizer =  WordNetLemmatizer()

lem=[]
for word in ss:
    lem.append(lemmatizer.lemmatize(word))

lem = set(lem)
lems = list(lem)

dictOfWords = { lems[i] : i for i in range(0, len(lems) ) }
print(dictOfWords)
#sentence = 'project this is arthur conan series with dorothea copyright'
sentence = input('Enter sentence or words: ')
sf = word_tokenize(sentence)
x= []

for i in sf:
    if dictOfWords.get(i) != None:
        x.append(dictOfWords.get(i))
    else:
        x.append(0)
        


sk=' '.join(str(xx) for xx in x)
padding = (20-len(x)) * ' 0'
print(sk + padding)