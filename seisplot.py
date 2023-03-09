import pandas as pd
import matplotlib.pyplot as plt

# Load data from text file
df = pd.read_csv('data.txt', delimiter='\s+')

# Drop duplicates
df = df.drop_duplicates(subset='DATE')

# Convert DATE column to datetime
df['DATE'] = pd.to_datetime(df['DATE'])

# Sort data by DATE
df = df.sort_values('DATE')

# Calculate time intervals in Hz
df['Hz'] = 1 / df['DATE'].diff().dt.total_seconds().fillna(0)

# Create four different types of plots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
axs[0, 0].plot(df['DATE'], df['MAG'], color='blue')
axs[0, 0].set_title('Magnitude vs. Date (Line Plot)')
axs[0, 0].set_xlabel('Date')
axs[0, 0].set_ylabel('Magnitude')

axs[0, 1].scatter(df['DATE'], df['MAG'], color='red')
axs[0, 1].set_title('Magnitude vs. Date (Scatter Plot)')
axs[0, 1].set_xlabel('Date')
axs[0, 1].set_ylabel('Magnitude')

axs[1, 0].hist(df['MAG'], bins=20, color='green')
axs[1, 0].set_title('Magnitude Distribution (Histogram)')
axs[1, 0].set_xlabel('Magnitude')
axs[1, 0].set_ylabel('Frequency')

axs[1, 1].plot(df['Hz'], df['MAG'], color='purple')
axs[1, 1].set_title('Magnitude vs. Frequency (Line Plot)')
axs[1, 1].set_xlabel('Frequency (Hz)')
axs[1, 1].set_ylabel('Magnitude')

# Adjust layout and display the plots
plt.tight_layout()
plt.show()
