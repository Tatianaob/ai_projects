# Spam mail detector. Using Scikit-Learn

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import seaborn as sns  #for data visualization
import matplotlib.pyplot as plt 

# load the dataset and split it into training and testing sets

data = pd.read_csv('spam.csv')
X = data.drop('spam', axis=1)
y = data['spam']

X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Logistic Regression model to classify emails as spam or not spam
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)


print(X_test)

# Evaluate the model using accuracy, confusion matrix, precision, recall and F1 score
accuracy = accuracy_score(y_test, y_pred)

