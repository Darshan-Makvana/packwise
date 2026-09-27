# PackWise – Smart Packing Checklist

A dynamic web app for travellers to build and manage a packing checklist.

## Features
- Add packing items with a name and category (e.g. Travel, Electronics)
- Mark items as packed / unpacked
- Delete items
- JSON API at `/api/items`
- Health check at `/health`
- Live commit ID shown in the footer

## Tech stack
- Python 3 + Flask
- Automated tests with pytest
- Lint with flake8
- CI/CD with GitHub Actions
- Hosted on Render

## Run locally
```
python -m venv venv
venv\Scripts\activate        (macOS/Linux: source venv/bin/activate)
pip install -r requirements.txt
pytest -v
python app.py
```
Then open http://localhost:5000

## Pipeline
1. **Lint + Test** — runs on every push and pull request
2. **Deploy** — runs only on push to `main`, and only if tests pass, by calling the Render deploy hook

## Live app
<PASTE YOUR RENDER URL HERE>

## Repository
<PASTE YOUR GITHUB URL HERE>
