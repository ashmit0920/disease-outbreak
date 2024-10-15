import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

data = pd.read_csv("google_trends.csv")

# Scale the data to 0-1 range for LSTM
scaler = MinMaxScaler(feature_range=(0, 1))
data_scaled = scaler.fit_transform(data[["covid"]])

# Create sequences of 30 days to predict the next day
X = []
y = []

sequence_length = 30
for i in range(sequence_length, len(data_scaled)):
    X.append(data_scaled[i-sequence_length:i, 0])
    y.append(data_scaled[i, 0])

X, y = np.array(X), np.array(y)

# Reshape X to be compatible with LSTM (samples, timesteps, features)
X = np.reshape(X, (X.shape[0], X.shape[1], 1))

# Build the LSTM model
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(X.shape[1], 1)))
model.add(LSTM(units=50))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X, y, epochs=20, batch_size=32)

# Predict the next day's search interest
predicted_search_interest = model.predict(X)
predicted_search_interest = scaler.inverse_transform(predicted_search_interest)

predicted_search_interest = np.round(predicted_search_interest, 0).astype(int)
# print(predicted_search_interest)
mse = mean_squared_error(y, predicted_search_interest)
mae = mean_absolute_error(y, predicted_search_interest)
r2 = r2_score(y, predicted_search_interest)

print(f"Mean Squared Error: {mse}")
print(f"Mean Absolute Error: {mae}")
print(f"R-squared: {r2}")