# Import section
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp

# Let's check the first 5 entry of the dataset
# using the CSV file
df = pd.read_csv('../data/raw/CarSales.csv')

# Change the column names to meaningful names
df.columns = ["symboling", "normalized-losses", "make",
              "fuel-type", "aspiration", "num-of-doors",
              "body-style", "drive-wheels", "engine-location",
              "wheel-base", "length", "width", "height", "curb-weight",
              "engine-type", "num-of-cylinders", "engine-size",
              "fuel-system", "bore", "stroke", "compression-ratio",
              "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]
# For now let's just save this meaningful headers to csv file
df.to_csv("../data/processed/CarSaleProcessed.csv", index=False)
# Check the first 5 entry
# print(df.head())
# Look for any missing or null values
data = df
print(data.isna().any())
print(data.isnull().any())