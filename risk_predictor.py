from pathlib import Path
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "risk_model.pkl"

def _dataset():
    rng = np.random.default_rng(42)
    rows = []
    for _ in range(1200):
        attendance = rng.uniform(45, 100)
        marks = rng.uniform(35, 95, 4)
        avg = marks.mean()
        # Transparent rule used only to create a reproducible teaching dataset.
        if avg < 50 or attendance < 55:
            label = "High Risk"
        elif avg < 65 or attendance < 70:
            label = "Medium Risk"
        else:
            label = "Low Risk"
        rows.append([attendance, *marks, label])
    return np.array(rows, dtype=object)

def train_and_save_model():
    data = _dataset()
    X = data[:, :5].astype(float)
    y = data[:, 5]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    model = RandomForestClassifier(n_estimators=150, random_state=42, class_weight="balanced")
    model.fit(X_train, y_train)
    score = accuracy_score(y_test, model.predict(X_test))
    MODEL_PATH.parent.mkdir(exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    return MODEL_PATH, score

def predict_risk(features):
    if not MODEL_PATH.exists():
        train_and_save_model()
    model = joblib.load(MODEL_PATH)
    return str(model.predict([features])[0])
