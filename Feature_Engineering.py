# Create new features
transaction_data['transaction_date'] = pd.to_datetime(transaction_data['date'])
transaction_data['year'] = transaction_data['transaction_date'].dt.year
transaction_data['month'] = transaction_data['transaction_date'].dt.month

# Aggregating data to create new features
transaction_summary = transaction_data.groupby('customer_id').agg({
    'amount': ['sum', 'mean', 'max', 'min'],
    'transaction_id': 'count'
}).reset_index()

transaction_summary.columns = ['customer_id', 'total_amount', 'avg_amount', 'max_amount', 'min_amount', 'transaction_count']

# Merge with customer data
customer_data = customer_data.merge(transaction_summary, on='customer_id', how='left')

print(customer_data.head())
