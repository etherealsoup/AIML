#SMART CITY
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("smart_city_traffic_dataset.csv")

X = data[['vehicles', 'time', 'weather', 'road_width']]
y = data['traffic_level']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

print("\n--- Smart City Traffic System ---")

vehicles = int(input("Enter number of vehicles: "))
time = int(input("Enter time (0-23): "))
weather = int(input("Weather (0=Clear, 1=Rain): "))
road_width = float(input("Enter road width: "))

user = pd.DataFrame([[vehicles, time, weather, road_width]],
                    columns=['vehicles','time','weather','road_width'])

prediction = model.predict(user)

# -------- OUTPUT SECTION --------

if prediction[0] == 0:
    traffic = "LOW 🚗"
elif prediction[0] == 1:
    traffic = "MEDIUM 🚦"
else:
    traffic = "HIGH 🚨"

if 17 <= time <= 20:
    peak = "YES 🚨"
else:
    peak = "NO"

if vehicles > 150:
    pollution = "HIGH 🌫️"
elif vehicles > 70:
    pollution = "MEDIUM"
else:
    pollution = "LOW"

if prediction[0] == 2:
    suggestion = "Use alternate routes or increase signal time."
elif prediction[0] == 1:
    suggestion = "Expect moderate delays."
else:
    suggestion = "Traffic is smooth."

print("\n--- Smart Analysis Result ---")
print("Traffic Level:", traffic)
print("Peak Hour:", peak)
print("Pollution Level:", pollution)
print("Suggestion:", suggestion)
