import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data_original/Blog-data-original.csv')
df_p = pd.read_csv('data_processed/Blog-data-preprocessed.csv')
wcount_original = pd.read_csv('data_processed/wcount-data-original.csv')
wcount_new = pd.read_csv('data_processed/wcount-data-processed.csv')

fig, ax = plt.subplots()
ax.set(title='Blogs Count',ylabel='Number of Blogs', xlabel='Website Name')
ax.bar(['AWS','Facebook'],[len(df[df['Website']=='AWS']),len(df[df['Website']=='Facebook'])])
fig.show()
fig.set_dpi(100)
fig.savefig('visuals/bar_blogscount.png',facecolor='w')  


fig, ax = plt.subplots()
ax.set(title='Blogs contribution from each website')
ax.pie([len(df[df['Website']=='AWS']),len(df[df['Website']=='Facebook'])],labels= ['AWS','Facebook'], autopct='%.2f%%', startangle=90)
fig.set_dpi(100)
fig.show()
fig.savefig('visuals/pie_total_blogs.png',facecolor='w') 


fig, ax = plt.subplots()
a = wcount_original[wcount_original['Website']=='AWS']['word_count'].sum()
b = wcount_original[wcount_original['Website']=='Facebook']['word_count'].sum()
print(a,b)
ax.set(title="Pie Chart showing each website's contribution towards Total words")
ax.pie([a,b],labels= ['AWS','Facebook'], autopct='%.2f%%', startangle=90)
fig.set_dpi(100)
fig.show()
fig.savefig('visuals/pie_total_words.png',facecolor='w') 


fig, ax = plt.subplots()
a1 = a - wcount_new[wcount_new['Website']=='AWS']['word_count'].sum()
b1 = b - wcount_new[wcount_new['Website']=='Facebook']['word_count'].sum()
print(a1,b1)
ax.set(title="Pie chart showing each website's contribution towards Total stop words.")
ax.pie([a1,b1],labels= ['AWS','Facebook'], autopct='%.2f%%', startangle=90)
fig.set_dpi(100)
fig.show()
fig.savefig('visuals/pie_stop_words.png',facecolor='w') 



fig, ax = plt.subplots()
x = ['Original data','Preprocessed data']
y = [wcount_original['word_count'].sum()/1000000, wcount_new['word_count'].sum()/1000000]
ax.set(title='Word count comparision in Millions',ylabel='Number of Blogs', xlabel='Type of data')
ax.bar(x,y, color=['blue','orange'])
fig.show()
fig.set_dpi(100)
fig.savefig('visuals/word_count_orig_vs_proc.png',facecolor='w') 


fig, ax = plt.subplots()
ax.set(title='Word Count',ylabel='Number of words in Millions', xlabel='Data')
a = wcount_original[wcount_original['Website']=='AWS']['word_count'].sum()/1000000
b = wcount_new[wcount_new['Website']=='AWS']['word_count'].sum()/1000000
c = wcount_original[wcount_original['Website']=='Facebook']['word_count'].sum()/1000000
d = wcount_new[wcount_new['Website']=='Facebook']['word_count'].sum()/1000000
ax.bar(['AWS_Orig','AWS_Proc','Facebook_orig','Facebook_proc'],[a,b,c,d], color=['blue','orange'])
fig.show()

colors = {'Original':'blue', 'Preprocessed':'Orange'}         
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
ax.legend(handles, labels)

fig.set_dpi(100)
fig.savefig('visuals/word_count_all.png',facecolor='w')  



import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer() 
vectors = vectorizer.fit_transform(df_p['content'])

tf_idf = pd.DataFrame(vectors.todense()).iloc[:5]  
tf_idf.columns = vectorizer.get_feature_names()
tfidf_matrix = tf_idf.T
tfidf_matrix.columns = ['Blog'+ str(i) for i in range(1, 6)]
tfidf_matrix['count'] = tfidf_matrix.sum(axis=1)
tfidf_matrix = tfidf_matrix.sort_values(by ='count', ascending=False)[:10] 
tfidf_matrix.to_string('data_processed/correlations.txt')
print(tfidf_matrix.drop(columns=['count']).head(10))

out = 'Word Count Summary for original dataset'
out = out  + '\n\n' + wcount_original['word_count'].describe().to_string()

out = out + '\n\n' + 'Word Count Summary for preprocessed dataset'
out = out + '\n\n' + wcount_new['word_count'].describe().to_string()

out = out + '\n\n' + 'Summary of stopwords count '
out  = out + '\n\n' + (wcount_original['word_count'] - wcount_new['word_count']).describe().to_string()

text_file = open("data_processed/summary.txt", "w")
text_file.write(out)
text_file.close()


fig, ax = plt.subplots()
ax.set(title='Word Count Scatter Plot',xlabel='Word count in original data',ylabel='Word count in Pre-processed data')
ax.scatter(wcount_original['word_count'],wcount_new['word_count'],alpha=0.8)
fig.set_dpi(100)
fig.show()
fig.savefig('visuals/scatter_1.png',facecolor='w') 

fig, ax = plt.subplots()
ax.set(title='Word Count of original Data vs Stopwords Scatter Plot',xlabel='Word count in original data',ylabel='Stop words count in the data')
ax.scatter(wcount_original['word_count'],wcount_original['word_count'] - wcount_new['word_count'],alpha=0.8)
fig.set_dpi(100)
fig.show()
fig.savefig('visuals/scatter_2.png',facecolor='w')

fig, ax = plt.subplots()
ax.set(title='Word Count of Preprocessed Data vs Stopwords Scatter Plot',xlabel='Word count in Preprocessed data',ylabel='Stop words count in the data')
ax.scatter(wcount_new['word_count'],wcount_original['word_count'] - wcount_new['word_count'],alpha=0.8)
fig.set_dpi(100)
fig.show()
fig.savefig('visuals/scatter_3.png',facecolor='w')