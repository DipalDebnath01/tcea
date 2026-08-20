import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Read CSV file
csv_path = os.path.join(os.path.dirname(__file__), "Salary_Data.csv")
data = pd.read_csv(csv_path)

print("===== Simple Linear Regression =====")

# Display dataset
print("\nDataset:")
print(data)

# Independent variable
X = data[["YearsExperience"]]

# Dependent variable
y = data["Salary"]

# Split data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Linear Regression model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict salary
y_pred = model.predict(X_test)

# Model information
print("\n===== Model Results =====")
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# Accuracy
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print("R² Score:", r2)
print("Mean Squared Error:", mse)

# User input
experience = float(
    input("\nEnter years of experience to predict salary: ")
)

predicted_salary = model.predict([[experience]])

print(
    "Predicted Salary: ₹",
    round(predicted_salary[0], 2)
)

# Plot graph
plt.figure(figsize=(10, 6))

plt.scatter(
    data["YearsExperience"],
    data["Salary"],
    label="Actual Data"
)

plt.plot(
    data["YearsExperience"],
    model.predict(data[["YearsExperience"]]),
    label="Regression Line"
)

plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Years of Experience vs Salary")

plt.legend()
plt.grid(True)

plt.show()