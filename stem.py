import unicodedata
import sys
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem.porter import *


def stemmed (chunk):
	stemmed_word=[]
	stemmer = PorterStemmer()
	for word in chunk:
		stemmed_word.append(stemmer.stem(word))

	return stemmed_word

def removeStopwords( chunk ):
	good = []
	for word in tokens:
	    if word not in stopwords.words('english'):
	        good.append(word)
	return good


#Main implementation
#Reading from file
with open ("filename.txt", "r") as myfile:
    sentence=myfile.read().replace('\n', '')

#reducing the sentece to all lower case letters
sentence = sentence.lower()

#tokenize the sentence
tokens = nltk.word_tokenize(sentence)

#removing punctuation and unicode characters
tokens = words = re.findall(r'\w+', sentence,flags = re.UNICODE | re.LOCALE)

#Remove stopwords from the list
important_words = []
important_words = removeStopwords(tokens)

#performing porter stemming
stu = []
stu = stemmed(important_words)


#performing the final correction 
final = []
for word in stu:
	if word not in final:
		final.append(word)

#remove numbers from the list
final = [item for item in final if item.isalpha()]
print final