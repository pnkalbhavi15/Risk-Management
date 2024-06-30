import pandas as pd
from faker import Faker
import random

fake = Faker()

# Generate synthetic transaction data
def generate_transaction_data(num_records):
    transactions = []
    for _ in range(num_records):
        transactions.append({
            'transaction_id': fake.uuid4(),
            'customer_id': fake.uuid4(),
            'date': fake.date_time_this_year(),
            'amount': round(random.uniform(10, 1000), 2),
            'type': random.choice(['credit', 'debit'])
        })
    return pd.DataFrame(transactions)

# Generate synthetic customer data
def generate_customer_data(num_customers):
    customers = []
    for _ in range(num_customers):
        customers.append({
            'customer_id': fake.uuid4(),
            'name': fake.name(),
            'email': fake.email(),
            'credit_score': random.randint(300, 850)
        })
    return pd.DataFrame(customers)

# Example usage
transaction_data = generate_transaction_data(1000)
customer_data = generate_customer_data(100)

# Save to CSV for easy loading later
transaction_data.to_csv('transaction_data.csv', index=False)
customer_data.to_csv('customer_data.csv', index=False)

print("Transaction Data Sample:")
print(transaction_data.head())

print("Customer Data Sample:")
print(customer_data.head())
