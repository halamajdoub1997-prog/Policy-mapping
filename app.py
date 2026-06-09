import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="HIV Policy Map Europe", layout="wide")

# -------------------------
# LOAD DATA
# -------------------------
df = pd.read_csv("data.csv")

# -------------------------
# SCORE CALCULATION
# -------------------------
agg = df.groupby(["country", "indicator"])["value"].mean().reset_index()
agg["score"] = agg["value"] * 100

overall = df.groupby("country")["value"].mean().reset_index()
overall["score"] = overall["value"] * 100
overall["indicator"] = "Overall Score"

map_df = pd.concat([agg, overall])

# -------------------------
# SIDEBAR FILTER
# -------------------------
st.sidebar.title("Filters")

indicator = st.sidebar.selectbox(
    "Select Policy Layer",
    sorted(map_df["indicator"].unique())
)

# -------------------------
# FILTER DATA
# -------------------------
filtered = map_df[map_df["indicator"] == indicator]

# -------------------------
# TITLE
# -------------------------
st.title("🌍 HIV Continuum of Care Policy Map for Migrants in Europe")
st.write("Interactive policy scoring based on national HIV prevention and care access indicators.")

# -------------------------
# MAP (Plotly Choropleth)
# -------------------------
fig = px.choropleth(
    filtered,
    locations="country",
    locationmode="country names",
    color="score",
    color_continuous_scale="RdYlGn",
    range_color=(0, 100),
    hover_name="country",
    title=f"{indicator} (Policy Inclusion Score)"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------
# TABLE VIEW
# -------------------------
st.subheader("📊 Country Scores")

st.dataframe(
    filtered.sort_values("score", ascending=False),
    use_container_width=True
)

# -------------------------
# EXPLANATION
# -------------------------
st.markdown("""
### 🧾 Scoring system
- 1 = policy exists / equal access
- 0 = no access / exclusion
- Scores are averaged per indicator and scaled 0–100

### 🧩 Layers include:
- PrEP access
- PEP access
- HIV testing
- STI testing
- ART treatment
- Monitoring
- Primary care access
""")
