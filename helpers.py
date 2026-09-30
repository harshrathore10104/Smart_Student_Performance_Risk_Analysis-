def risk_from_score(attendance, average_marks):
    if average_marks < 50 or attendance < 55:
        return "High Risk"
    if average_marks < 65 or attendance < 70:
        return "Medium Risk"
    return "Low Risk"
