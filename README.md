# Salary Prediction Using Simple Linear Regression

## Project Overview

This project predicts an employee's salary based on their years of experience using Simple Linear Regression.

The project uses a salary dataset containing information about years of experience and corresponding salary.

## Objective

The main objective of this project is to build a simple machine learning model that can predict salary based on the number of years of work experience.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

## Dataset

The dataset used in this project is `Salary_Data.csv`.

The dataset contains two main columns:

- YearsExperience
- Salary

## Methodology

The following steps are performed in this project:

1. Load the salary dataset.
2. Read and analyze the data using Pandas.
3. Separate the input and output variables.
4. Split the dataset into training and testing data.
5. Train a Simple Linear Regression model.
6. Calculate the model performance.
7. Display the actual data and regression line using a graph.
8. Take years of experience as user input.
9. Predict the expected salary.

## Machine Learning Algorithm

### Simple Linear Regression

Simple Linear Regression is used to find the relationship between two variables.

In this project:

- Independent Variable: Years of Experience
- Dependent Variable: Salary

The equation of the regression line is:

Salary = m × YearsExperience + c

Where:

- m = slope
- c = intercept

## Model Results

The program displays:

- Slope
- Intercept
- R² Score
- Mean Squared Error
- Predicted Salary

## Graph

The project generates a graph showing:

- Actual salary data points
- Regression line

The graph represents the relationship between years of experience and salary.

## How to Run the Project

Open the project folder in Visual Studio Code and run:

```bash
python simple_linear_regression.py