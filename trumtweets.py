# -*- coding: utf-8 -*-
"""
Created on Wed May  6 06:08:24 2020

"""

#read json file
import pandas as pd
df = pd.read_json("C:/Users/gurdd/Desktop/ml/spacy/trumptwitter_latest year.json")

#tweets
tweets = ""
for i,j in df.iterrows():
    tweets += ' '
    tweets += j["text"]
    
#load package
import spacy
nlp = spacy.load('en')

#inc max length from 1 ml to 3 ml
nlp.max_length = 3000000 

#Reading a Doc or Text

#when you call your spaCy pipeline, disable RAM-hungry intensive parts of the pipeline you don't need for lemmatization

#Read text/token
#docx = nlp(tweets), disable = ['ner', 'parser'])
docx = nlp(tweets)


# Remove stop word
from spacy.lang.en.stop_words import STOP_WORDS
docx2 = [word for word in docx if word.is_stop == False] 

docx3 = [word for word in docx2 if ((len(word) != 1) & (len(word) < 20))] 

# List Comprehensions of our Lemma
docx4 = [word.lemma_.lower().strip() for word in docx3]

###############################################################################
###############################################################################
###############################################################################
###############################################################################

# 1. Num of countries mentioned
# 2. No of people mentioned
# 3. How many times he said China, CNN, Fake News, NY Times, impeachment, coronavirus, whuhan, covid19
# 4. most used words
# 5. No of tweets per day
# 6. No of tweets grouped by time of the day

###############################################################################
###############################################################################
###############################################################################
###############################################################################

###############################################################################
#1. Number of Countries
###############################################################################
from collections import Counter

badchar = ['â','€','@','ðÿ‘‡ðÿ','œa','à¤”à¤','à¤¤','à¥‡à¤','à¤•à¥‹','ø§ø']

docx5 = ''
for mystr in docx4:
  if all(x not in mystr for x in badchar):
      docx5 = docx5 + mystr
      docx5 = docx5 + ' '
      
docx6 = docx5.split()

text = ''
for word in docx6:
    text = text + word
    text = text+ ' '
    
wikitext = nlp(text)

GPE = [word for word in wikitext.ents if (word.label_ == 'GPE')]

countries = [ent.text for ent in wikitext.ents if ent.label_ == 'GPE']

countrylist = Counter(countries).most_common(100)

print(Counter(countries).most_common(10))

###############################################################################
#2. Number of Twitter references
###############################################################################

twitterref = ['@']

twitterid = ''
for mystr in docx4:
  if all(x in mystr for x in badchar):
      twitterid = twitterid + mystr
      twitterid = twitterid + ' '
      
name = [word for word in docx4 if word.startswith('@')]

name_ref =  Counter(name).most_common(100)

###############################################################################
#3. How many times trump said China, CNN, Fake News, NY Times, impeachment, coronavirus, whuhan, covid19, fox
###############################################################################

freqwords = ['china','cnn','fake','nytimes','impeachment','coronavirus','wuhan','covid19', 'fox']

list3 = [x for x in docx4 if x in freqwords]

# Python code to count the number of occurrences 
def countX(lst, x): 
    count = 0
    for ele in lst: 
        if (ele == x): 
            count = count + 1
    return count 

for x in freqwords:
    print('{} has occurred {} times'.format(x, countX(list3, x))) 

###############################################################################
# 4. most used words
###############################################################################

from collections import Counter

badchar = ['â','€','@','ðÿ‘‡ðÿ','œa','à¤”à¤','à¤¤','à¥‡à¤','à¤•à¥‹','ø§ø']

docx5 = ''
for mystr in docx4:
  if all(x not in mystr for x in badchar):
      docx5 = docx5 + mystr
      docx5 = docx5 + ' '
      
mostcommon = Counter(docx5).most_common(100)

print(mostcommon)

###############################################################################
# 4. most used words
###############################################################################

import spacy
from collections import Counter

nlp = spacy.load('en')
qwer = nlp(tweets)
type(qwer)

# Remove Punct,Stop 
text1 = [token.text for token in qwer if token.is_stop != True and token.is_punct !=True]

word_freq = Counter(text1)

common_words = word_freq.most_common(10)

print(common_words)

###############################################################################
# 5. No of tweets per day
###############################################################################

from datetime import datetime

df['created_at_date'] = df['created_at'].dt.date

df.groupby(['created_at_date']).count()

###############################################################################
# 6. No of tweets grouped by time of the day
###############################################################################

from datetime import datetime

df['created_at_hour'] = df['created_at'].dt.hour

df2 = df.groupby(['created_at_hour']).count()
df2['hour'] = df2.index

import matplotlib.pyplot as plt

df2.plot('hour', 'created_at', kind='bar', title ="Number of tweets per hour", figsize=(15, 10), legend=True, fontsize=12)
plt.show()

