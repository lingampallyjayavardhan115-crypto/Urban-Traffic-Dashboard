import pandas as pd

# Load datasets from Google Drive or Colab environment
traffic = pd.read_csv("/content/traffic.csv")
pollution = pd.read_csv("/content/pollution.csv")
weather = pd.read_csv("/content/weather.csv")
regions = pd.read_csv("/content/regions.csv")

# Clean traffic data
traffic['timestamp'] = pd.to_datetime(traffic['timestamp'])
traffic = traffic.dropna(subset=['vehicle_count'])

# Clean pollution data
pollution = pollution.drop_duplicates()
pollution['AQI'] = pollution['AQI'].fillna(pollution['AQI'].mean())

# Clean weather data
weather['date'] = pd.to_datetime(weather['date'])
weather['rainfall'] = weather['rainfall'].fillna(0)

# Merge datasets
merged = traffic.merge(pollution, on="location") \
                .merge(weather, on="station_id") \
                .merge(regions, on="zone_name")

# Save cleaned dataset
merged.to_csv("/content/cleaned_data.csv", index=False)

print("✅ Cleaned dataset saved as cleaned_data.csv")
