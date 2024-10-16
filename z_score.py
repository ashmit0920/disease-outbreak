import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_csv("malaria.csv")
search_term = "malaria"

data['z_score'] = (data[search_term] - data[search_term].mean()) / data[search_term].std()

# Set a threshold for anomaly detection (e.g., |z_score| > 1.5)
anomaly_threshold = 1.5
data['anomaly'] = np.where(data['z_score'].abs() > anomaly_threshold, 1, 0)

data_outbreak = data[data['anomaly'] == 1]
print(data_outbreak)

plt.figure(figsize=(10, 6))
plt.bar(data_outbreak['date'], data_outbreak[search_term], color='blue', linewidth=2)

plt.title(f"Times when outbreak is detected for {search_term}", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Interest (0-100)", fontsize=12)

plt.xticks(rotation=90)

plt.grid(True)
plt.tight_layout()
plt.show()

# Raise alert if anomaly is detected (check last recorded anomaly data for live data)
if data['anomaly'].iloc[-1] == 1:
    print("ALERT: Possible outbreak detected due to spike in search interest!")