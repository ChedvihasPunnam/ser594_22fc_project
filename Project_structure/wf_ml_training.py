import pandas as pd
import pickle
import warnings
warnings.filterwarnings("ignore")

x_train = pd.read_csv(r"models\x_train.csv")
x_test = pd.read_csv(r"models\x_test.csv")
y_train = pd.read_csv(r"models\y_train.csv")
y_test = pd.read_csv(r"models\y_test.csv")


x_data = x_train
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
lin_r= LinearRegression()
lin_r.fit(x_train,y_train)
pickle.dump(lin_r, open(r'models\linear_regression.pkl', 'wb'))

lr= LogisticRegression()
lr.fit(x_data,y_train)
pickle.dump(lr, open(r'models\logistic_regression.pkl', 'wb'))



from sklearn.neighbors import KNeighborsClassifier
K = KNeighborsClassifier(n_neighbors = 3)
K.fit(x_train[20:], y_train[20:])
print(K.score)
pickle.dump(lr, open(r'models\KNN.pkl', 'wb'))



