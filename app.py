import streamlit as st

st.set_page_config(page_title="HIV Policy Interpretation Tool", layout="wide")

st.title("HIV Continuum of Care for Migrants")
st.caption("Policy interpretation tool (definition layer, not dataset table)")

# ---------------- DATA MODEL ----------------
data = {
    "Primary Prevention": [
        {
            "indicator": "PrEP Access Equity",
            "meaning": "Assesses whether national policy ensures equal PrEP access for migrants and undocumented migrants.",
            "migrants": "Included / Not included (based on national law)",
            "undocumented": "Included / Not included (based on national law)",
            "free": "Free at point of care: Yes / No",
            "interpretation": "Measures equity in preventive HIV medication access."
        },
        {
            "indicator": "Condom Distribution Inclusion",
            "meaning": "Assesses whether migrants are included in national condom distribution programmes.",
            "migrants": "Included / Not included",
            "undocumented": "Included / Not included",
            "free": "Not applicable / Depends on programme",
            "interpretation": "Measures access to basic prevention commodities."
        }
    ],

    "Secondary Prevention": [
        {
            "indicator": "PEP Access Equity",
            "meaning": "Assesses access to post-exposure prophylaxis for migrants.",
            "migrants": "Included / Not included",
            "undocumented": "Included / Not included",
            "free": "Free at point of care: Yes / No",
            "interpretation": "Measures emergency HIV prevention accessibility."
        }
    ],

    "Diagnosis": [
        {
            "indicator": "HIV Testing Access",
            "meaning": "Assesses whether migrants can access HIV testing services equally.",
            "migrants": "Included / Not included",
            "undocumented": "Included / Not included",
            "free": "Free at point of care: Yes / No",
            "interpretation": "Measures early diagnosis accessibility."
        },
        {
            "indicator": "STI Testing Access",
            "meaning": "Assesses access to STI screening services.",
            "migrants": "Included / Not included",
            "undocumented": "Included / Not included",
            "free": "Free at point of care: Yes / No",
            "interpretation": "Measures broader sexual health service access."
        }
    ],

    "Linkage to Care": [
        {
            "indicator": "Care Pathways Availability",
            "meaning": "Assesses whether structured pathways exist from testing to treatment.",
            "migrants": "Available / Not available",
            "undocumented": "Available / Not available",
            "free": "Not applicable",
            "interpretation": "Measures continuity of care after diagnosis."
        }
    ],

    "Treatment": [
        {
            "indicator": "ART Access Equity",
            "meaning": "Assesses access to antiretroviral therapy for migrants.",
            "migrants": "Included / Not included",
            "undocumented": "Included / Not included",
            "free": "Free at point of care: Yes / No",
            "interpretation": "Measures treatment access equity."
        },
        {
            "indicator": "ART Initiation Policy",
            "meaning": "Assesses eligibility for ART regardless of CD4 count.",
            "migrants": "Eligible / Restricted",
            "undocumented": "Eligible / Restricted",
            "free": "Not applicable",
            "interpretation": "Measures alignment with WHO treat-all strategy."
        }
    ],

    "Care": [
        {
            "indicator": "Primary Healthcare Access",
            "meaning": "Assesses access to general healthcare services.",
            "migrants": "Included / Not included",
            "undocumented": "Included / Not included",
            "free": "Depends on system",
            "interpretation": "Measures integration into national health system."
        }
    ]
}

# ---------------- UI ----------------

for domain, indicators in data.items():
    with st.expander(f"🔵 {domain}", expanded=False):

        for item in indicators:

            st.markdown("---")

            with st.container():

                st.markdown(f"## 🧾 {item['indicator']}")

                # Meaning (VERY IMPORTANT)
                st.info(f"🧠 {item['meaning']}")

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("### 👥 Population Coverage")
                    st.write("• Migrants:", item["migrants"])
                    st.write("• Undocumented:", item["undocumented"])

                with col2:
                    st.markdown("### 💰 Cost / Access Condition")
                    st.write(item["free"])

                st.markdown("### 📘 Interpretation")
                st.success(item["interpretation"])
