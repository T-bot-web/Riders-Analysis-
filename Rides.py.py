# ===============================
# Bike Riders Analysis Dashboard Code
# ===============================

# 1. Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Load CSV file
df = pd.read_csv("BikeRiders_Analysis.csv")

# 3. Basic data check
print("Shape:", df.shape)
print("\nColumns:\n", df.columns)
print("\nInfo:")
df.info()

# 4. Handle missing values
df.fillna(0, inplace=True)

# 5. Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# 6. Create new time-based columns
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day

# ===============================
# KPI CALCULATIONS
# ===============================

# Total Rides
total_rides = df["ride_id"].nunique()

# Total Riders
total_riders = df["rider_id"].nunique()

# Total Revenue
total_revenue = df["fare_amount"].sum()

# Average Fare
average_fare = df["fare_amount"].mean()

print("\n--- KPIs ---")
print("Total Rides:", total_rides)
print("Total Riders:", total_riders)
print("Total Revenue:", total_revenue)
print("Average Fare:", average_fare)

# ===============================
# DASHBOARD AGGREGATIONS
# ===============================

# City-wise Revenue
city_revenue = df.groupby("city")["fare_amount"].sum().reset_index()

# Monthly Rides
monthly_rides = df.groupby("month")["ride_id"].count().reset_index()

# Rider Type Analysis
rider_type = df.groupby("rider_type")["ride_id"].count().reset_index()

# ===============================
# VISUALIZATIONS
# ===============================

# City-wise Revenue
plt.figure(figsize=(8,5))
sns.barplot(data=city_revenue, x="city", y="fare_amount")
plt.title("City-wise Revenue")
plt.xticks(rotation=45)
plt.show()

# Monthly Ride Trend
plt.figure(figsize=(8,5))
sns.lineplot(data=monthly_rides, x="month", y="ride_id", marker="o")
plt.title("Monthly Ride Trend")
plt.xlabel("Month")
plt.ylabel("Number of Rides")
plt.show()

# Rider Type Distribution
plt.figure(figsize=(6,6))
plt.pie(rider_type["ride_id"], labels=rider_type["rider_type"], autopct="%1.1f%%")
plt.title("Rider Type Distribution")
plt.show()

# ===============================
# EXPORT CLEAN DATA FOR POWER BI / TABLEAU
# ===============================

df.to_csv("clean_bike_riders_data.csv", index=False)
city_revenue.to_csv("city_revenue.csv", index=False)
monthly_rides.to_csv("monthly_rides.csv", index=False)
rider_type.to_csv("rider_type_summary.csv", index=False)

print("\nFiles exported successfully for dashboard use.")
