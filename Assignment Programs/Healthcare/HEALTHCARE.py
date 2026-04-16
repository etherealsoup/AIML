#HEALTHCARE
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = pd.read_csv("healthcare_diabetes_clean.csv")

X = data[['Glucose', 'BloodPressure', 'BMI', 'Age']]
y = data['Outcome']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

print("\n--- Enter Patient Details ---")

glucose = float(input("Enter Glucose level: "))
bp = float(input("Enter Blood Pressure: "))
bmi = float(input("Enter BMI: "))
age = float(input("Enter Age: "))

user_data = pd.DataFrame(
    [[glucose, bp, bmi, age]],
    columns=['Glucose', 'BloodPressure', 'BMI', 'Age']
)
prediction = model.predict(user_data)

if prediction[0] == 1:
    print("\nResult: High Risk of Diabetes ⚠️")
    print("Advice: Please consult a doctor and maintain a healthy lifestyle.")
else:
    print("\nResult: Low Risk of Diabetes ✅")
    print("Advice: Keep maintaining your healthy habits!")
