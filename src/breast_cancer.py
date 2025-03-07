from sklearn.datasets import load_breast_cancer
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

cancer = load_breast_cancer()
print cancer.keys()
# print cancer['DESCR']
print cancer['feature_names']
print cancer['data'].shape

X = cancer['data']
Y = cancer['target']

X_train, X_test, y_train, y_test = train_test_split(X, Y)

scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Train
mlp = MLPClassifier(hidden_layer_sizes=(30, 30, 30))
mlp.fit(X_train, y_train)
print mlp

predictions = mlp.predict(X_test)
print confusion_matrix(y_test, predictions)
print classification_report(y_test, predictions)

print len(mlp.coefs_)
print len(mlp.coefs_[0])
print len(mlp.intercepts_[0])
print mlp.predict(X_test[1:4])
