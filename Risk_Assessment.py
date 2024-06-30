# Predict risk for new data
new_data = X_test.copy()  # Replace with actual new data
risk_predictions = model.predict(new_data)
new_data['risk_prediction'] = risk_predictions

print(new_data.head())
