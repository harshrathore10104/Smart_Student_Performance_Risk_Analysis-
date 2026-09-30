import pandas as pd
from modules.performance_analyzer import calculate_metrics

def test_metrics():
    df = pd.DataFrame({"average_marks": [50, 70, 90]})
    result = calculate_metrics(df)
    assert result["mean_marks"] == 70
    assert result["max_marks"] == 90
    assert result["min_marks"] == 50
