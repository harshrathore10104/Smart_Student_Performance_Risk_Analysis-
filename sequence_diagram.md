# Sequence Diagram

```text
User -> Streamlit: Enter student data
Streamlit -> Validator: Validate values
Validator --> Streamlit: Valid
Streamlit -> Database: Insert record
Database --> Streamlit: Success
User -> Streamlit: Request risk prediction
Streamlit -> Risk Model: Predict(features)
Risk Model --> Streamlit: Risk class
Streamlit --> User: Display result
```
