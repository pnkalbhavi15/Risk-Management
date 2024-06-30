import pandas as pd

# Load the generated data
transaction_data = pd.read_csv('transaction_data.csv')
customer_data = pd.read_csv('customer_data.csv')

# Display the first few rows of each dataset
print(transaction_data.head())
print(customer_data.head())

# Basic data analysis
print("Transaction Data Statistics:")
print(transaction_data.describe())

print("Customer Data Statistics:")
print(customer_data.describe())
