import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("Weather_Disease_Spread_dataset.csv")

df['Disease Spread'] = df['Disease Type'].apply(lambda x: 1 if x == 'Vector-borne' else 0)

features = ['Temperature (°C)', 'Humidity (%)', 'Precipitation (mm)', 'Wind Speed (km/h)', 'Air Pressure (hPa)', 'Disease Spread']

df = df[features]

features = ['Temperature (°C)', 'Humidity (%)', 'Precipitation (mm)', 'Wind Speed (km/h)', 'Air Pressure (hPa)']

scaler = MinMaxScaler()
df[features] = scaler.fit_transform(df[features])

X = df[features]
y = df['Disease Spread']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

def classifier_model():
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    return clf
