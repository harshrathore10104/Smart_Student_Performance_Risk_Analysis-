# Smart Student Performance & Risk Analysis System

A Python-based academic analytics application developed for the VITyarthi Build Your Own Project evaluation.

## Features
- Student record management using SQLite
- Academic performance analytics
- Attendance and marks visualization
- Machine learning risk classification
- Interactive Streamlit dashboard
- PDF student report generation
- Input validation
- Automated tests

## Technology Stack
Python, Streamlit, SQLite, Pandas, NumPy, Scikit-learn, Plotly, ReportLab, Joblib, Pytest.

## Installation

```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run:
```bash
streamlit run app.py
```

## Testing
```bash
pytest -q
```

## Project Modules
- `app.py` - user interface
- `database/` - SQLite data layer
- `modules/performance_analyzer.py` - analytics
- `modules/risk_predictor.py` - ML model
- `modules/report_generator.py` - PDF reports
- `utils/` - validation/helper functions
- `tests/` - automated tests

## ML Note
The included dataset is synthetic and intended for academic demonstration. The model should not be treated as a real-world diagnostic or high-stakes decision system.

## Git Workflow
```bash
git init
git add .
git commit -m "Initial project implementation"
git branch -M main
git remote add origin <YOUR_GITHUB_REPOSITORY_URL>
git push -u origin main
```
