import os
import nltk
import nltk.corpus


# inspect corpora modules, classes and methods
print(os.listdir(nltk.data.find('corpora')))
print('\n')

# inspect corpora
print(nltk.corpus.gutenberg.fileids())
print('\n')

#extract text
hamlet = nltk.corpus.gutenberg.words('shakespeare-macbeth.txt')
print(hamlet)
print('\n')

#extract full text
for word in hamlet[:30]:
    print(word, sep=' ')
print('\n')



#create your own text
MU = '''Mzumbe University was established by the Mzumbe University Charter, 
        2007 under Section 25 of the Universities Act. No. 7 of 2005 
        which repealed Mzumbe University Act. No 9 of 2001. As a Training 
        Institute, the University boasts of over 50 years experience of training 
        in the administration of justice, business management, public administration, 
        accountancy, finance, political science and good governance.
    '''
from nltk.tokenize import word_tokenize
MU_tokens = word_tokenize(MU)
print(MU_tokens)
print('\n')
print(len(MU_tokens))
print('\n')

#check frequency of tokens
from nltk.probability import FreqDist
fdict = FreqDist()
for word in MU_tokens:
    fdict[word.lower()] += 1
print(fdict)
print('\n')

#check frequency of particular word 
print(fdict['mzumbe'])
print('\n')

#check number of distinct words
print(len(fdict))
print('\n')

#selecting top words ten with high feq
fdict_top10 = fdict.most_common(10)
print(fdict_top10)
print('\n')









#using blankline method instead of word_tokenize
from nltk.tokenize import blankline_tokenize
MU_blank = blankline_tokenize(MU)
print(MU_blank)
print(len(MU_blank)) # checks number of paragraphs
print('\n')

#read second paragraph
print(MU_blank[0])
print('\n')









#Unigrams, Bigrams, Trigrams, Ngrams
#Unigrams
from nltk.util import bigrams, trigrams, ngrams
string = 'The boy is runningi the shell now.'
quotes_tokens = nltk.word_tokenize(string)
print(quotes_tokens)

#Bigrams
quotes_bigrams = list(nltk.bigrams(quotes_tokens))
print(quotes_bigrams)

#Trigrams
quotes_trigrams = list(nltk.trigrams(quotes_tokens))
print(quotes_trigrams)

#Ngrams
quotes_ngrams = list(nltk.ngrams(quotes_tokens, 4))
print(quotes_ngrams)
print('\n')







#stemming - normalize words into its base or root form
# using poster stemmer
from nltk.stem import PorterStemmer
pst = PorterStemmer()
words_to_stem = ['give', 'giving', 'given', 'gave']
for words in words_to_stem:
    print(words + ': ' + pst.stem(words))
print('\n')

# using lancaster stemmer
from nltk.stem import LancasterStemmer
lst = LancasterStemmer()
for words in words_to_stem:
    print(words + ': ' + lst.stem(words))
print('\n')

# using snawball stemmer
from nltk.stem import SnowballStemmer
sbst = SnowballStemmer('english') #needs to specify language
for words in words_to_stem:
    print(words + ': ' + sbst.stem(words))
print('\n')

#usung lemmatizer - out upt of this is a proper word
from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()
for words in words_to_stem:
    print(words + ': ' + wnl.lemmatize(words))
print('\n')










#stop words
from nltk.corpus import stopwords
stop_w = stopwords.words('english')
print(stop_w)
print('\n')
print(len(stop_w))
print('\n')










#removing non words
import re
panctuations = re.compile(r'[-.?!,:;()|0-9]')
post_panctuation = []
for words in MU_tokens:
    word = panctuations.sub('', words)
    if len(word) > 0:
        post_panctuation.append(word)
print(post_panctuation)
print('\n')









#POS - Parts of speech
sent = 'Tomas is a human color when it comes to names.'
sent_token = word_tokenize(sent)
for token in sent_token:
    print(nltk.pos_tag([token]))






#NER - Named entity recognition eg: location, person, qnty, money, facility, org, movie
from nltk import ne_chunk
NE_sent = 'The Uni President stays in his house'
NE_tokens = word_tokenize(NE_sent)
NE_tags = nltk.pos_tag([NE_tokens])
NE_ner = ne_chunk(NE_tags)
print(NE_ner)
