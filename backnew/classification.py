import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC


def prepare_data(cols, data):
    x = pd.DataFrame(data=data, dtype='float32', columns=cols)
    x.fillna(method='ffill', inplace=True)
    return x


def prepare_har():
    x_train = pd.read_csv('har1.csv')
    x_train.drop('Label', inplace=True, axis=1)
    x_train.drop(x_train.columns[0], inplace=True, axis=1)
    y_train = pd.read_csv('har1.csv', usecols=['Label'])
    return x_train, y_train


def glcm_ada(x):
    X_train_har, y_train_har = prepare_har()
    ada = AdaBoostClassifier(n_estimators=500, random_state=42)
    ada.fit(X_train_har, y_train_har)
    pred = ada.predict(x)
    return pred


def glcm_rf(x):
    X_train_har, y_train_har = prepare_har()
    rf = RandomForestClassifier(n_estimators=500, criterion='entropy', random_state=42)
    rf.fit(X_train_har, y_train_har)
    pred = rf.predict(x)
    return pred

def glcm_svm(x):
    X_train_har, y_train_har = prepare_har()
    svm = SVC(C=100.0, random_state=0)
    svm.fit(X_train_har, y_train_har)
    pred = svm.predict(x)
    return pred


def glcm_mlp(x):
    X_train_har, y_train_har = prepare_har()
    scaler = StandardScaler()
    x_train = scaler.fit_transform(X_train_har)
    mlp = MLPClassifier(hidden_layer_sizes=(100,), activation='logistic', solver='adam', alpha=1e-4,
                        max_iter=1000, random_state=1)
    mlp.fit(x_train, y_train_har)
    pred = mlp.predict(x)
    return pred


def glcm_knn(x):
    X_train_har, y_train_har = prepare_har()
    knn = KNeighborsClassifier(n_neighbors=9)
    knn.fit(X_train_har, y_train_har)
    pred = knn.predict(x)
    return pred


def prepare_lbp():
    x_train = pd.read_csv('lbp1.csv')
    x_train.drop('Label', inplace=True, axis=1)
    x_train.drop(x_train.columns[0], inplace=True, axis=1)
    y_train = pd.read_csv('lbp1.csv', usecols=['Label'])
    return x_train, y_train


def lbp_ada(x):
    X_train, y_train = prepare_lbp()
    ada = AdaBoostClassifier(n_estimators=500, random_state=42)
    ada.fit(X_train, y_train)
    pred = ada.predict(x)
    return pred


def lbp_rf(x):
    X_train, y_train = prepare_lbp()
    rf = RandomForestClassifier(n_estimators=500, criterion='entropy', random_state=42)
    rf.fit(X_train, y_train)
    pred = rf.predict(x)
    return pred


def lbp_mlp(x):
    X_train, y_train = prepare_lbp()
    scaler = StandardScaler()
    x_train = scaler.fit_transform(X_train)
    mlp = MLPClassifier(hidden_layer_sizes=(100,), activation='logistic', solver='adam', alpha=1e-4,
                        max_iter=1000, random_state=1)
    mlp.fit(x_train, y_train)
    pred = mlp.predict(x)
    return pred


def lbp_knn(x):
    X_train, y_train = prepare_lbp()
    knn = KNeighborsClassifier(n_neighbors=9)
    knn.fit(X_train, y_train)
    pred = knn.predict(x)
    return pred


def prepare_zer():
    x_train = pd.read_csv('zer.csv')
    x_train.drop('Label', inplace=True, axis=1)
    x_train.drop(x_train.columns[0], inplace=True, axis=1)
    y_train = pd.read_csv('zer.csv', usecols=['Label'])
    return x_train, y_train


def zer_ada(x):
    X_train, y_train = prepare_zer()
    ada = AdaBoostClassifier(n_estimators=500, random_state=42)
    ada.fit(X_train, y_train)
    pred = ada.predict(x)
    return pred


def zer_rf(x):
    X_train, y_train = prepare_zer()
    rf = RandomForestClassifier(n_estimators=500, criterion='entropy', random_state=42)
    rf.fit(X_train, y_train)
    pred = rf.predict(x)
    return pred


def zer_mlp(x):
    X_train, y_train = prepare_zer()
    scaler = StandardScaler()
    x_train = scaler.fit_transform(X_train)
    mlp = MLPClassifier(hidden_layer_sizes=(100,), activation='logistic', solver='adam', alpha=1e-4,
                        max_iter=1000, random_state=1)
    mlp.fit(x_train, y_train)
    pred = mlp.predict(x)
    return pred


def zer_knn(x):
    X_train, y_train = prepare_zer()
    knn = KNeighborsClassifier(n_neighbors=9)
    knn.fit(X_train, y_train)
    pred = knn.predict(x)
    return pred


def prepare_law():
    x_train = pd.read_csv('law1.csv')
    x_train.drop('Label', inplace=True, axis=1)
    x_train.drop(x_train.columns[0], inplace=True, axis=1)
    y_train = pd.read_csv('law1.csv', usecols=['Label'])
    return x_train, y_train


def law_ada(x):
    X_train, y_train = prepare_law()
    ada = AdaBoostClassifier(n_estimators=500, random_state=42)
    ada.fit(X_train, y_train)
    pred = ada.predict(x)
    return pred


def law_rf(x):
    X_train, y_train = prepare_law()
    rf = RandomForestClassifier(n_estimators=500, criterion='entropy', random_state=42)
    rf.fit(X_train, y_train)
    pred = rf.predict(x)
    return pred


def law_mlp(x):
    X_train, y_train = prepare_law()
    scaler = StandardScaler()
    x_train = scaler.fit_transform(X_train)
    mlp = MLPClassifier(hidden_layer_sizes=(100,), activation='logistic', solver='adam', alpha=1e-4,
                        max_iter=1000, random_state=1)
    mlp.fit(x_train, y_train)
    pred = mlp.predict(x)
    return pred


def law_knn(x):
    X_train, y_train = prepare_law()
    knn = KNeighborsClassifier(n_neighbors=9)
    knn.fit(X_train, y_train)
    pred = knn.predict(x)
    return pred
