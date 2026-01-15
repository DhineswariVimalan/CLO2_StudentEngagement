import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load dataset
data = pd.read_csv(
    r"C:\Users\user\CLO2_StudentEngagement\data\student_engagement.csv"
)

# Features
X = data[
    ['total_clicks',
     'active_days',
     'interactive_clicks',
     'content_clicks',
     'inter_ratio']
]

# Target
y = data['engagement_level']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Random Forest model (Model v2)
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Model v2 Accuracy:", accuracy)

# Save model
with open('model_v2.pkl', 'wb') as f:
    pickle.dump(model, f)

print("model_v2.pkl saved successfully")