import pandas as pd
import matplotlib.pyplot as plt

article_df = pd.read_csv("articles.csv")

daily_counts = article_df.groupby('date').size().reset_index(name='count')

# Calculate the rolling average to smooth the data and observe trends
daily_counts['rolling_avg'] = daily_counts['count'].rolling(window=3).mean()

# Define a threshold for spikes (e.g., 2x the rolling average or a sudden jump)
threshold = 1.4

# Flag days where the count exceeds the threshold
daily_counts['spike_flag'] = daily_counts['count'] > (threshold * daily_counts['rolling_avg'])
print(daily_counts)

# Print the dates where spikes were detected
outbreak_dates = daily_counts[daily_counts['spike_flag']]

print("Outbreak detected on these dates:")
print(outbreak_dates[['date', 'count']])

plt.figure(figsize=(10, 6))

# Plot the daily counts of keyword mentions
plt.plot(daily_counts['date'], daily_counts['count'], label='Keyword Mentions')

# Plot the rolling average
plt.plot(daily_counts['date'], daily_counts['rolling_avg'], label='3-Day Rolling Average', linestyle='--')

# Highlight dates where outbreaks are flagged
plt.scatter(outbreak_dates['date'], outbreak_dates['count'], color='red', label='Outbreak Flagged')

plt.xticks(rotation=90)
plt.xlabel('Date')
plt.ylabel('Keyword Mentions')
plt.title('Trend of Disease Outbreak Mentions Over Time')
plt.legend()
plt.grid(True)
plt.show()
