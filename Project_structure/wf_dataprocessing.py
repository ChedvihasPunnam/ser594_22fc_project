import numpy as np
import pandas as pd
import regex as re
import string
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

df = pd.read_csv('data_original\Blog-data-original.csv')

print(df[df.isnull().any(axis=1)])

df = df.dropna()

df_p = df.dropna()

print(df[df.isnull().any(axis=1)])

df_p['content'] = df_p['Title'].str.replace("[^\w\s]|[_]", " ") + ' ' +  df['content']

#to lowercase all the text
df_p['content'] = df_p['content'].str.lower()

#to remove punctuations
df_p['content'] = df_p['content'].str.replace("[^\w\s]|[_]", " ")

#to remove any digits or numerical data
df_p['content'] = df_p['content'].str.replace('\d+', ' ')
df_p['content'] = df_p['content'].replace(r'\s+', ' ')

lemmatizer = WordNetLemmatizer()
stop_words = stopwords.words('english')
df_p['content'] = df_p['content'].apply(lambda x: ' '.join([word.strip() for word in x.split() if word not in (stop_words)]))
df_p['content'] = df_p['content'].apply(lambda x: ' '.join([lemmatizer.lemmatize(word.strip(),pos='v') for word in x.split()]))

df_p.to_csv('data_processed/Blog-data-preprocessed.csv',index=False)




wcount_original = pd.DataFrame({'Website':[],'Title':[],'word_count':[]})
print(wcount_original)
wcount_new = pd.DataFrame({'Website':[],'Title':[],'word_count':[]})
t = df['content'] + df['Title']

wcount_original['Website'] = df['Website']
wcount_original['Title'] = df['Title']

temp = []
for i in df['content']:
    temp.append(len(i))


wcount_original['word_count'] = temp

wcount_original.to_csv('data_processed/wcount-data-original.csv',index=False)

wcount_new['Website'] = df['Website']
wcount_new['Title'] = df['Title']
temp = []
for j in df_p['content']:
    temp.append(len(j))

wcount_new['word_count'] = temp

wcount_new.to_csv('data_processed/wcount-data-processed.csv',index=False)

