import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import Ridge
import warnings
warnings.filterwarnings("ignore")

lr = pickle.load(open(r'models\logistic_regression.pkl', 'rb'))
lin_r = pickle.load(open(r'models\linear_regression.pkl', 'rb'))
K = pickle.load(open(r'models\KNN.pkl', 'rb'))


x_test = pd.read_csv(r"models\x_test.csv")
y_test = pd.read_csv(r"models\y_test.csv")

x_test.reset_index(drop=True)

# cleaning input text for prediction
text = input('Enter text to predict keywords: ')
text = text.lower()
import string
text = text.translate(str.maketrans('', '', string.punctuation))
text1 = ''
for i in text.split():
    if len(i)>1:
            text1 = text1 + ' ' + i
text = text1
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
text_tokens = word_tokenize(text)

text = [word for word in text_tokens if not word in stopwords.words()]
text = ' '.join(text)

text = text.split()
test_d = {'word':text}

from sklearn.preprocessing import LabelEncoder

le_word=LabelEncoder()
test_df = pd.DataFrame(test_d)
test_df["nword"]=le_word.fit_transform(test_df["word"])
test_df = test_df.drop_duplicates()

#print(test_df)

x_test = pd.read_csv('data_processed\Blog-data-preprocessed.csv')

test_df_main = x_test[100:120]
test_df_main = test_df_main[['content']]
test_df_main.reset_index(drop=True)
test_df_main.loc[len(test_df_main.index)] = [' '.join(text)]
test_df_main.reset_index(drop=True)


from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
tfvec = TfidfVectorizer()
tdf = tfvec.fit_transform(test_df_main['content'])
bow_test = pd.DataFrame(tdf.toarray(), columns = tfvec.get_feature_names())
bow_test


res = []
[res.append(x) for x in text if x not in res]
probs = {}
for i in res:
    LR_out = lin_r.predict([[test_df[test_df['word']==i]['nword'],bow_test[i].sum()]])
    probs[i] = LR_out

import operator

sorted_x = sorted(probs.items(), key=operator.itemgetter(1))
sorted_x = [i[0] for i in sorted_x]
print("====================================Linear Regression results=============================")
print(sorted_x[-5:])



for i in res:
    K_out = K.predict([[test_df[test_df['word']==i]['nword'],bow_test[i].sum()]])
    probs[i] = K_out

import operator

sorted_x = sorted(probs.items(), key=operator.itemgetter(1))
sorted_x = [i[0] for i in sorted_x]
print("====================================KNN results=============================")
print(sorted_x[-5:])

probs = {}
for i in res: 
    
    out = lr.predict_proba([[test_df[test_df['word']==i]['nword'],bow_test[i].sum()]])[0][1]
    
    
    probs[i]= out

import operator

sorted_x = sorted(probs.items(), key=operator.itemgetter(1))
sorted_x = [i[0] for i in sorted_x]
print("====================================Logistic Regression results=============================")
print(sorted_x[-5:])





