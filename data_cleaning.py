import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\jayal\Desktop\Travel-Tourism-Analytics\dataset\hotel_booking.csv")

# Check missing values
print("Missing Values:")
print(df.isnull().sum())

# Fill missing values
df["children"] = df["children"].fillna(0)
df["country"] = df["country"].fillna("Unknown")
df["agent"] = df["agent"].fillna(0)
df["company"] = df["company"].fillna(0)

# Remove duplicate rows
df = df.drop_duplicates()

# Convert date columns (if needed)
df["reservation_status_date"] = pd.to_datetime(df["reservation_status_date"])

# Save cleaned dataset
df.to_csv(r"C:\Users\jayal\Desktop\Travel-Tourism-Analytics\dataset\hotel_booking_cleaned.csv", index=False)

print("\nData cleaning completed successfully!")
print("New Shape:", df.shape)