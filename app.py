import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style

data = pd.read_csv("student-mat.csv",sep=';')
data = data[['G1','G2','G3','studytime','failures','absences']]
predict = 'G3'

x = np.array(data.drop([predict],1))
# Real notes
y = np.array(data[predict])

best = 0
for _ in range(30):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print(acc)

    if (acc > best):
        best = acc
        # Pickle dumps train data
        with open("studentmodel.pickle", "wb") as f:
            pickle.dump(linear, f)
print('best:',best)

# Open data from pickle without train anymore
with open('studentmodel.pickle', 'rb') as f:
    pickle_in = pickle.load(f)
linear = pickle_in

print("Co:", linear.coef_)
print("Intercept:", linear.intercept_)

predictions = linear.predict(x_test)

# results analysis
for x in range(len(predictions)):
    print("Test params:", x_test[x],"Real:",y_test[x],"Predition:%.2f"%predictions[x],)

