from sklearn.naive_bayes import BernoulliNB
import numpy as np
import pandas as pd
from sklearn import *
from sklearn.metrics import accuracy_score
df = pd.read_csv('powerset.csv')
df["BatterySize"] = df["BatterySize"].map({'High':2 ,'Medium':1,'Low':0})
data = df[["AverageLoad","PeakLoad","MedianLoad","RatedPVpower","AnnualConsumption","AccumualtedEnergy","UtilizationHours","InjectionHours","PowerDrawn","PowerInjected","BatterySize"]].to_numpy()
inputs = data[:,:-1]
outputs = data[:, -1]
training_inputs = inputs[:300]
training_outputs = outputs[:300]
testing_inputs = inputs[300:]
testing_outputs = outputs[300:]
classifier = BernoulliNB()
classifier.fit(training_inputs, training_outputs)
predictions = classifier.predict(testing_inputs)
accuracy = 100.0 * accuracy_score(testing_outputs, predictions)
print ("The accuracy of BNB Classifier on testing data is: " + str(accuracy))
testSet = [[0.14,0.67,0.24,6,654,378,4184,3092,1.57,4]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('BNBC prediction on the first test set is:',predictions)
testSet = [[0.61,7.6,0.92,10,4513,7992,5534,2928,5.28,10.48]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('BNBC prediction on the second test set is:',predictions)
testSet = [[2.25,36.08,8.74,17,45873,26005,6599,1104,28.92,12.59]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('BNBC prediction on the third test set is:',predictions)

