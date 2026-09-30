# GitHub Upload Guide

Do not upload `venv` or `.venv`. They are intentionally excluded.
GitHub will recreate the environment from `requirements.txt`.

## Commands

```bash
git init
git add .
git commit -m "Initial project submission"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/Smart-Student-Performance-Risk-Analysis.git
git push -u origin main
```

## Run after cloning

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m streamlit run app.py
```
