from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Sample target variable (e.g., binary risk indicator based on credit score)
customer_data['risk'] = customer_data['credit_score'].apply(lambda x: 1 if x < 600 else 0)

# Select features and target
features = ['total_amount', 'avg_amount', 'max_amount', 'min_amount', 'transaction_count']
X = customer_data[features]
y = customer_data['risk']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
