import pandas as pd

# Load the data
transaction_data = pd.read_csv('transaction_data.csv')
customer_data = pd.read_csv('customer_data.csv')

# Check for missing values
print(transaction_data.isnull().sum())
print(customer_data.isnull().sum())

# Handle missing values (if any)
# transaction_data.fillna(method='ffill', inplace=True)
# customer_data.fillna(method='ffill', inplace=True)
