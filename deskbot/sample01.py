## Importing the necessary libraries
import nltk
import random
import string # to process standard python strings


## Corpus - is the training data needed for the chatbot to learn
## Reading in the data
# We will read in the corpus.txt file and convert the entire corpus into a list of
# sentences and a list of words for further pre-processing.
f=open('deskbot/sample01.txt', 'r', errors = 'ignore')
raw=f.read()
raw=raw.lower()# converts to lowercase
sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences
word_tokens = nltk.word_tokenize(raw)# converts to list of words


## Pre-processing the raw text
# We shall now define a function called LemTokens which will take as input the
# tokens and return normalized tokens.
lemmer = nltk.stem.WordNetLemmatizer()
# WordNet is a semantically-oriented dictionary of English included in NLTK.
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


## Keyword matching
# Next, we shall define a function for a greeting by the bot i.e if a user’s input is a
# greeting, the bot shall return a greeting response.
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


## Generating Response
#To generate a response from our bot for input questions, the concept of
#document similarity will be used.
# This will be used to find the similarity between words entered by the user and the
# words in the corpus.
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# We define a function response which searches the user’s utterance for one or
# more known keywords and returns one of several possible responses. If it doesn’t
# find the input matching any of the keywords, it returns a response:” I am sorry! I
# don’t understand you”
def response(user_response):
    bot_response=''
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize,
    stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        bot_response=bot_response+"I am sorry! I don't understand you"
        return bot_response
    else:
        bot_response = bot_response+sent_tokens[idx]
        return bot_response


def get_response(user_response):
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            return "You are welcome.."
        else:
            if(greeting(user_response)!=None):
                return greeting(user_response)
            else:
                sent_tokens.append(user_response)
                word_tokens=word_tokens+nltk.word_tokenize(user_response)
                final_words=list(set(word_tokens))
                sent_tokens.remove(user_response)
                return response(user_response)
    else:
        return "Bye! take care.."

