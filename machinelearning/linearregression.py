import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt  
import seaborn as sns  
from sklearn.model_selection import train_test_split  
from sklearn.linear_model import LinearRegression  
from sklearn.metrics import mean_absolute_error, mean_squared_error  

print( )

# Create a sample dataset
data = {
    'Size (sqft)': [750, 800, 850, 900, 950, 1000, 1100, 1200, 1300, 1400],
    'Bedrooms': [1, 2, 2, 3, 3, 3, 4, 4, 5, 5],
    'Age': [10, 15, 20, 25, 30, 35, 10, 15, 5, 2],
    'Price': [150000, 160000, 170000, 180000, 200000, 220000, 250000, 270000, 300000, 320000]
}

df = pd.DataFrame(data)
print(df.head())  # Show first 5 rows


# Correlation Heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.show()

# Scatter plot: Size vs Price
plt.figure(figsize=(6, 4))
sns.scatterplot(x=df['Size (sqft)'], y=df['Price'])
plt.xlabel("Size (sqft)")
plt.ylabel("Price ($)")
plt.title("Size vs Price")
plt.show()

X = df[['Size (sqft)', 'Bedrooms', 'Age']]  # Features
y = df['Price']  # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()  # Create Linear Regression Model
model.fit(X_train, y_train)  # Train the model

y_pred = model.predict(X_test)  # Predict prices for test data
print("Predicted Prices:", y_pred)


mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f"Mean Absolute Error (MAE): {mae}")
print(f"Mean Squared Error (MSE): {mse}")
print(f"Root Mean Squared Error (RMSE): {rmse}")

plt.figure(figsize=(6, 4))
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted Prices")
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red')  # Perfect Fit Line
plt.show()
