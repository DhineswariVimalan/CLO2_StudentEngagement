import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pickle
# Load dataset
data = pd.read_csv('C:\\Users\\user\\CLO2_StudentEngagement\\data\\student_engagement.csv')
X = data.drop('target', axis=1)  # Features
y = data['target']               # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Initialize and train model
model_v1 = LogisticRegression(max_iter=1000)
model_v1.fit(X_train, y_train)
# Make predictions
y_pred = model_v1.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
# Save the trained model
with open('models/model_v1.pkl', 'wb') as f:
    pickle.dump(model_v1, f)