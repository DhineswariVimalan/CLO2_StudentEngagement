import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

# Load dataset
data = pd.read_csv(
    r"C:\Users\user\CLO2_StudentEngagement\data\student_engagement.csv"
)

# Features (X)
X = data[
    ['total_clicks',
     'active_days',
     'interactive_clicks',
     'content_clicks',
     'inter_ratio']
]

# Target (y)
y = data['engagement_level']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Logistic Regression model (Model v1)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Model v1 Accuracy:", accuracy)

# Save model
with open('model_v1.pkl', 'wb') as f:
    pickle.dump(model, f)

print("model_v1.pkl saved successfully")