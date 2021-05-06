from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report

cancer_data=load_breast_cancer()
X = cancer_data.data
Y = cancer_data.target
print('Input Data size :',X.shape)
print('Output Data size :',Y.shape)
print('Label names :',cancer_data.target_names)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state=42)
clf= SVC(kernel='linear',C=1.0,random_state=42)
clf.fit(X_train,Y_train)

accuracy=clf.score(X_test,Y_test)
print(f'The accuracy is: {accuracy*100:.1f}%')
pred=clf.predict(X_test)
print(classification_report(Y_test, pred,target_names=cancer_data.target_names))