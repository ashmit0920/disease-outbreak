from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt

pytrends = TrendReq(hl='en-US', tz=360)

search_term = "covid"
pytrends.build_payload([search_term], cat=0, timeframe='2019-07-01 2024-03-01', geo='', gprop='') # geo='' for global trends

data = pytrends.interest_over_time()

# Remove 'isPartial' column if it exists
if 'isPartial' in data.columns:
    data = data.drop(columns=['isPartial'])

print(data.head())

data.to_csv("google_trends.csv")

plt.figure(figsize=(10, 6))
plt.plot(data.index, data[search_term], color='blue', linewidth=2)

plt.title(f"Search Interest for '{search_term}' globally (2019-2024)", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Interest (0-100)", fontsize=12)

plt.xticks(rotation=45)

plt.grid(True)
plt.tight_layout()
plt.show()