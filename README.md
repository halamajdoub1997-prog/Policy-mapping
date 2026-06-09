# 🌍 HIV Policy Continuum for Migrants in Europe

Interactive Streamlit dashboard mapping national HIV-related health access policies for migrants and undocumented migrants.

## Features
- 🇪🇺 Interactive Europe choropleth map
- 🧩 Policy layer selector (PrEP, PEP, testing, treatment, care)
- 📊 Country-level scoring (0–100)
- 📄 Data table view
- ⚡ Fully open-source Streamlit app

## Scoring logic
- 1 = policy allows equal access
- 0 = restricted or not allowed
- Scores are averaged per indicator

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
