import nltk
import re
import time
from nltk.stem import WordNetLemmatizer
from nltk.stem import SnowballStemmer


def onlyNounsAndNames(content):
    try:
        tokenized = nltk.word_tokenize(content)
        tagged = nltk.pos_tag(tokenized)
        words = ' '.join(word for word,tag in tagged if tag in ('NN', 'NNP') and word != ' Mr')
        return words
    except Exception, e:
        print str(e)


def lemmatizer(content):
    try:
        wordnet_lemmatizer = WordNetLemmatizer()
        tokenized = nltk.word_tokenize(content)
        tagged = nltk.pos_tag(tokenized)
        words = ' '.join(wordnet_lemmatizer.lemmatize(word, 'v') for word in tagged)
        return words
    except Exception, e:
        print str(e)

def stemmer(content):
    try:
        stemmer = SnowballStemmer()
        words = ' '.join(stemmer = SnowballStemmer((word, 'v') for word in tagged)
        return words
    except Exception, e:
        print str(e)
