from modules.risk_predictor import train_and_save_model, predict_risk

def test_model_prediction():
    _, score = train_and_save_model()
    assert 0 <= score <= 1
    result = predict_risk([90, 85, 80, 88, 92])
    assert result in {"Low Risk", "Medium Risk", "High Risk"}
