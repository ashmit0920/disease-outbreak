import pandas as pd
import matplotlib.pyplot as plt

article_df = pd.read_csv("articles.csv")

daily_counts = article_df.groupby('date').size().reset_index(name='count')

# Calculate the rolling average to smooth the data and observe trends
daily_counts['rolling_avg'] = daily_counts['count'].rolling(window=7).mean()

# Define a threshold for spikes (e.g., 2x the rolling average or a sudden jump)
threshold = 1.5

# Flag days where the count exceeds the threshold
daily_counts['spike_flag'] = daily_counts['count'] > (threshold * daily_counts['rolling_avg'])
print(daily_counts)

# Print the dates where spikes were detected
outbreak_dates = daily_counts[daily_counts['spike_flag']]

print("Outbreak detected on these dates:")
print(outbreak_dates[['date', 'count']])
