import pandas as pd

def calculate_metrics(df):
    return {
        "mean_marks": float(df["average_marks"].mean()),
        "max_marks": float(df["average_marks"].max()),
        "min_marks": float(df["average_marks"].min()),
    }

def subject_summary(df):
    cols = {
        "Mathematics": "mathematics",
        "DBMS": "dbms",
        "Python": "python",
        "Machine Learning": "machine_learning",
    }
    return pd.DataFrame([
        {"subject": name, "average": float(df[col].mean())}
        for name, col in cols.items()
    ])
