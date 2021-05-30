import numpy as np
import pandas as pd
from pandas._config.config import reset_option
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn import utils

df = pd.read_csv("insurance.csv")
print(df)

x=df.iloc[:,0]
y=df.iloc[:,1]

y = np.array(y)
y = y.reshape(-1, 1)
print(y.shape)

X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)
print(type(X_train), type(y_train))
encoded = np.array(y_train)
X_train = np.array(X_train)
#encoded = y_train.reshape(-1,1)
X_train = X_train.reshape(-1,1)
print(type(X_train), type(encoded))
# y_test = np.array(y_test)
# X_test = np.array(X_test)
# y_test = y_test.reshape(-1,1)
# X_test = X_test.reshape(-1,1)
# print(X_test.shape, y_test.shape)

lab_enc=preprocessing.LabelEncoder()
encoded=lab_enc.fit_transform(encoded.ravel())

def models(X_train,Y_train):
    #Using Logistic Regression 
    from sklearn.linear_model import LogisticRegression
    log = LogisticRegression(random_state = 0)
    log.fit(X_train, Y_train)

    #Using KNeighborsClassifier 
    from sklearn.neighbors import KNeighborsClassifier
    knn = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
    knn.fit(X_train, Y_train)

    #Using SVC linear
    from sklearn.svm import SVC
    svc_lin = SVC(kernel = 'linear', random_state = 0)
    svc_lin.fit(X_train, Y_train)

    #Using SVC rbf
    from sklearn.svm import SVC
    svc_rbf = SVC(kernel = 'rbf', random_state = 0)
    svc_rbf.fit(X_train, Y_train)

    #Using GaussianNB 
    from sklearn.naive_bayes import GaussianNB
    gauss = GaussianNB()
    gauss.fit(X_train, Y_train)

    #Using DecisionTreeClassifier 
    from sklearn.tree import DecisionTreeClassifier
    tree = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
    tree.fit(X_train, Y_train)

    #Using RandomForestClassifier method of ensemble class to use Random Forest Classification algorithm
    from sklearn.ensemble import RandomForestClassifier
    forest = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
    forest.fit(X_train, Y_train)

    #print model accuracy on the training data.
    print('[0]Logistic Regression Training Accuracy:', log.score(X_train, Y_train))
    print('[1]K Nearest Neighbor Training Accuracy:', knn.score(X_train, Y_train))
    print('[2]Support Vector Machine (Linear Classifier) Training Accuracy:', svc_lin.score(X_train, Y_train))
    print('[3]Support Vector Machine (RBF Classifier) Training Accuracy:', svc_rbf.score(X_train, Y_train))
    print('[4]Gaussian Naive Bayes Training Accuracy:', gauss.score(X_train, Y_train))
    print('[5]Decision Tree Classifier Training Accuracy:', tree.score(X_train, Y_train))
    print('[6]Random Forest Classifier Training Accuracy:', forest.score(X_train, Y_train))

print(X_train.shape, encoded.shape)
models(X_train, encoded)
