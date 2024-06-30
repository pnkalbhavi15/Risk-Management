import matplotlib.pyplot as plt
import seaborn as sns

# Visualize transaction amounts
plt.figure(figsize=(10, 6))
sns.histplot(transaction_data['amount'], bins=50, kde=True)
plt.title('Transaction Amount Distribution')
plt.show()

# Visualize customer credit scores
plt.figure(figsize=(10, 6))
sns.histplot(customer_data['credit_score'], bins=50, kde=True)
plt.title('Customer Credit Score Distribution')
plt.show()

# Analyze relationships
plt.figure(figsize=(10, 6))
sns.boxplot(x='type', y='amount', data=transaction_data)
plt.title('Transaction Amount by Type')
plt.show()
