from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,mean_absolute_error,mean_absolute_percentage_error
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
df = pd.read_csv('data_processed\Blog-data-preprocessed.csv')

dfs = df[:120]

from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
tfvec = TfidfVectorizer()
tdf = tfvec.fit_transform(dfs['content'])
bow = pd.DataFrame(tdf.toarray(), columns = tfvec.get_feature_names())

count=0
c = 0
d = {}
for i in dfs['content']:
    for j in i.split():
        if j in dfs['keywords'][count]:
            d[j] = 1
            
            c+=1
        else:
            if j not in d:
                d[j] = 0
    count+=1

nd = {'word':list(d.keys()),'Probability':list(d.values())}

ndf = pd.DataFrame(nd)

ndf['length'] = ndf.word.str.len()
ndf = ndf[ndf.length>1]
ndf = ndf.reset_index(drop=True)
del ndf['length']

count = 0
ndf['score'] = ''
for i in bow.sum():
    ndf['score'][count] = bow.sum()[ndf['word'][count]]
    
    count+=1

from sklearn.preprocessing import LabelEncoder
le_word=LabelEncoder()
ndf["nword"]=le_word.fit_transform(ndf["word"])

#Splitting train,test data
X = ndf[['nword','score']]
Y = ndf['Probability']
x_train, x_test,y_train,y_test = train_test_split(X,Y,test_size =0.2, shuffle=False)




x_train.to_csv(r'models\x_train.csv',index=False)
x_train.to_csv(r'data_processed\x_train.csv',index=False)
x_test.to_csv(r'models\x_test.csv',index=False)
x_test.to_csv(r'data_processed\x_test.csv',index=False)
y_train.to_csv(r'models\y_train.csv',index=False)
y_train.to_csv(r'data_processed\y_train.csv',index=False)
y_test.to_csv(r'models\y_test.csv',index=False)
y_test.to_csv(r'data_processed\y_test.csv',index=False)


#!/usr/bin/python
import wf_ml_training, wf_ml_prediction


#Logistic Regression
# print("==========================================================Logistic Regression=======================================================")
l_mse= mean_squared_error(wf_ml_prediction.y_test, wf_ml_prediction.lr.predict(x_test))
l_mae= mean_absolute_error(wf_ml_prediction.y_test, wf_ml_prediction.lr.predict(x_test))
l_rmse= np.sqrt(l_mse)


# print('Mean Square Error: ',l_mse)
# print('Mean Absolute Error: ',l_mae)
# print('Root Mean Squared Error: ',l_rmse)


#Linear Regression
lr_mse= mean_squared_error(wf_ml_prediction.y_test, wf_ml_prediction.lin_r.predict(x_test))
lr_mae= mean_absolute_error(wf_ml_prediction.y_test, wf_ml_prediction.lin_r.predict(x_test))
lr_rmse= np.sqrt(lr_mse)
# print("==========================================================Linear Regression=======================================================")
# print('Mean Square Error: ',lr_mse)
# print('Mean Absolute Error: ',lr_mae)
# print('Root Mean Squared Error: ',lr_rmse)

#KNN
#print("==========================================================KNN=====================================================================")
mse= mean_squared_error(y_test, wf_ml_prediction.K.predict(x_test))
mae= mean_absolute_error(y_test, wf_ml_prediction.K.predict(x_test))
rmse= np.sqrt(mse)
# print('Mean Square Error: ',mse)
# print('Mean Absolute Error: ',mae)
# print('Root Mean Squared Error: ',rmse)


with open(r"evaluation\summary.txt", "w") as f:
        
        
        f.write("==========================================================Logistic Regression=======================================================")
        f.write('\n')
        f.write("Mean Square Error: ")
        f.write(str(l_mse))
        f.write('\n')
        f.write("Mean absolute Error: ")
        f.write(str(l_mae))
        f.write('\n')
        f.write('Root Mean Square Error: ')
        f.write(str(l_rmse))
        f.write("\n")

        
        f.write("==========================================================Linear Regression=======================================================")
        f.write('\n')
        f.write("Mean Square Error: ")
        f.write(str(lr_mse))
        f.write('\n')
        f.write('Mean Absolute Error: ')
        f.write(str(lr_mae))
        f.write('\n')
        f.write('Root Mean Square Error: ')
        f.write(str(lr_rmse))
        f.write("\n")

        f.write("==========================================================KNN=====================================================================")
        f.write('\n')
        f.write("Mean Square Error: ")
        f.write(str(mse))
        f.write("\n")
        f.write('Mean Absolute Error:')
        f.write(str(mae))
        f.write("\n")
        f.write('Root Mean Square Error:')
        f.write(str(rmse))
        f.write("\n")
