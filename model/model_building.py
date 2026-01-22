# model_building.py
import pandas as pd
import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

# ── 1. Load dataset ───────────────────────────────────────
wine = load_wine()
X = pd.DataFrame(wine.data, columns=wine.feature_names)
y = wine.target   # 0,1,2

print("Class distribution:\n", pd.Series(y).value_counts())

# ── 2. Select 6 features ──────────────────────────────────
selected_features = [
    'flavanoids',
    'od280/od315_of_diluted_wines',
    'color_intensity',
    'proline',
    'alcohol',
    'hue'
]

X = X[selected_features]

# ── 3. Preprocessing ──────────────────────────────────────
# No missing values in this dataset → skip imputation

# Scale features (very important)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ── 4. Train-test split ───────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.25, random_state=42, stratify=y
)

# ── 5. Model ──────────────────────────────────────────────
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=8,
    random_state=42
)

model.fit(X_train, y_train)

# ── 6. Evaluate ───────────────────────────────────────────
y_pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['Cultivar 0', 'Cultivar 1', 'Cultivar 2']))

# ── 7. Save model + scaler ────────────────────────────────
os.makedirs("model", exist_ok=True)

joblib.dump(model,  "model/wine_cultivar_model.joblib")
joblib.dump(scaler, "model/scaler.joblib")

print("\nModel and scaler saved successfully.")