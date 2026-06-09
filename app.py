import streamlit as st
import pandas as pd
import plotly.express as px
from utils import compute_scores

st.set_page_config(layout="wide")

# -----------------------
# LOAD DATA
# -----------------------
df = pd.read_csv("data.csv")

df, domain_df, overall_df = compute_scores(df)

# -----------------------
# SIDEBAR
# -----------------------
st.sidebar.title("Filters")

domain_filter = st.sidebar.selectbox(
    "Select domain",
    ["Overall"] + list(df["domain"].unique())
)

# -----------------------
# MAP DATA
# -----------------------
if domain_filter == "Overall":
    map_df = overall_df
    color_col = "total_score"
else:
    map_df = domain_df[domain_df["domain"] == domain_filter]
    map_df = map_df.groupby("country")["domain_score"].mean().reset_index()
    color_col = "domain_score"

# -----------------------
# EUROPE MAP
# -----------------------
st.title("🌍 HIV Policy Map for Migrants in Europe")

fig = px.choropleth(
    map_df,
    locations="country",
    locationmode="country names",
    color=color_col,
    color_continuous_scale="RdYlGn",
    range_color=(0, 100),
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------
# CLICK-LIKE SIMULATION (Streamlit limitation workaround)
# -----------------------
st.subheader("🔎 Select Country")

country = st.selectbox("Choose a country", sorted(df["country"].unique()))

country_df = df[df["country"] == country]
country_domain = domain_df[domain_df["country"] == country]

# -----------------------
# COUNTRY PAGE
# -----------------------
st.markdown(f"## 🇪🇺 {country}")

overall_score = overall_df[overall_df["country"] == country]["total_score"].values[0]

st.metric("Overall Score", f"{overall_score:.1f} / 100")

# -----------------------
# DOMAIN SCORES
# -----------------------
st.subheader("📊 Domain Scores")

st.dataframe(country_domain[["domain", "domain_score"]])

# -----------------------
# INDICATOR BREAKDOWN
# -----------------------
st.subheader("📌 Indicator Breakdown")

st.dataframe(country_df[[
    "domain",
    "indicator",
    "weight",
    "si",
    "weighted"
]])
