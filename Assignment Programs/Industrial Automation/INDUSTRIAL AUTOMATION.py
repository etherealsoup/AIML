#INDUSTRIAL AUTOMATION

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("industrial_dataset.csv")

X = data[['temperature', 'vibration', 'pressure', 'runtime']]
y = data['failure']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

print("\n--- Industrial Machine Monitoring System ---")

temp = float(input("Enter Temperature: "))
vibration = float(input("Enter Vibration: "))
pressure = float(input("Enter Pressure: "))
runtime = float(input("Enter Runtime (hours): "))

user = pd.DataFrame([[temp, vibration, pressure, runtime]],
                    columns=['temperature','vibration','pressure','runtime'])

prediction = model.predict(user)

if prediction[0] == 1:
    status = "AT RISK ⚠️"
else:
    status = "SAFE ✅"

if temp > 120 or vibration > 70 or runtime > 20:
    risk = "HIGH 🚨"
elif temp > 90 or vibration > 40:
    risk = "MEDIUM ⚠️"
else:
    risk = "LOW"

warnings = []
if temp > 100:
    warnings.append("High Temperature 🌡️")
if vibration > 50:
    warnings.append("High Vibration ⚙️")
if pressure > 140:
    warnings.append("High Pressure 💨")

if prediction[0] == 1:
    suggestion = "Perform immediate maintenance!"
elif risk == "MEDIUM ⚠️":
    suggestion = "Schedule maintenance soon."
else:
    suggestion = "Machine is operating normally."

print("\n--- Machine Analysis ---")
print("Status:", status)
print("Risk Level:", risk)

if warnings:
    print("Warnings:", ", ".join(warnings))
else:
    print("Warnings: None")

print("Suggestion:", suggestion)
