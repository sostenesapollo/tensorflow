"""

 This code example reads an irregular data and do something
 that i don't know yet

 Car_Evaluation_DataSet


"""
import numpy as np
import pandas as pd
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
from sklearn import linear_model, preprocessing
import sklearn

data = pd.read_csv('car.data',sep=',')

# The preprocessing.LabelEncoder() will replace to integer values

le = preprocessing.LabelEncoder()

buying = le.fit_transform(list(data["buying"]))
maint = le.fit_transform(list(data["maint"]))
door = le.fit_transform(list(data["door"]))
persons = le.fit_transform(list(data["persons"]))
cls = le.fit_transform(list(data["class"]))
safety = le.fit_transform(list("safety"))
lug_boot = le.fit_transform(list("lug_boot"))

predict = "class"

x = list(zip(buying, maint, door, persons, lug_boot, safety))
y = list(cls)


x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)


model = KNeighborsClassifier(n_neighbors=5)
model.fit(x_train, y_train)
acc = model.score(x_test,y_test)
print(acc)

#print(data)
#print(door)