import streamlit as st

st.set_page_config(page_title="HIV Continuum - Migrants", layout="wide")

st.title("HIV Continuum of Care for Migrants")
st.caption("Policy definition explorer (not a dataset table)")

# ---------------- DATA ----------------
data = {
    "Primary Prevention": {
        "PrEP Access": [
            {
                "title": "PrEP access for migrants",
                "allowed": "Migrants can access PrEP at the same level as citizens",
                "not_allowed": "Migrants cannot access PrEP at the same level as citizens"
            },
            {
                "title": "PrEP access for undocumented migrants",
                "allowed": "Undocumented migrants can access PrEP at the same level as citizens",
                "not_allowed": "Undocumented migrants cannot access PrEP at the same level as citizens"
            },
            {
                "title": "PrEP free at point of care",
                "allowed": "Migrants can access PrEP for free at point of care",
                "not_allowed": "Migrants cannot access PrEP for free at point of care"
            }
        ],

        "Condom Distribution": [
            {
                "title": "Condom access for migrants",
                "allowed": "Migrants are included in condom distribution programmes",
                "not_allowed": "Migrants are excluded from condom distribution programmes"
            }
        ]
    },

    "Secondary Prevention": {
        "PEP Access": [
            {
                "title": "PEP access for migrants",
                "allowed": "Migrants can access PEP at the same level as citizens",
                "not_allowed": "Migrants cannot access PEP at the same level as citizens"
            }
        ]
    },

    "Diagnosis": {
        "HIV Testing": [
            {
                "title": "HIV testing for migrants",
                "allowed": "Migrants can access HIV testing at the same level as citizens",
                "not_allowed": "Migrants cannot access HIV testing at the same level as citizens"
            }
        ]
    },

    "Linkage to Care": {
        "Care Pathways": [
            {
                "title": "Linkage to care pathways",
                "allowed": "Clear pathways exist for migrants (testing → treatment → care)",
                "not_allowed": "No clear pathways exist for migrants"
            }
        ]
    },

    "Treatment": {
        "ART Access": [
            {
                "title": "ART access for migrants",
                "allowed": "Migrants can access first-line ARVs per national policy",
                "not_allowed": "Migrants cannot access first-line ARVs per national policy"
            },
            {
                "title": "ART access for undocumented migrants",
                "allowed": "Undocumented migrants can access ARVs at same level as citizens",
                "not_allowed": "Undocumented migrants cannot access ARVs at same level as citizens"
            },
            {
                "title": "ART initiation regardless of CD4",
                "allowed": "Migrants can start ART regardless of CD4 count",
                "not_allowed": "ART only available below CD4 threshold"
            }
        ],

        "Monitoring": [
            {
                "title": "Annual viral load & CD4 monitoring",
                "allowed": "At least once per year monitoring is allowed",
                "not_allowed": "Annual monitoring is not guaranteed"
            }
        ]
    },

    "Care": {
        "Primary Healthcare": [
            {
                "title": "Primary healthcare access",
                "allowed": "Migrants can access primary healthcare at same level as citizens",
                "not_allowed": "Migrants cannot access primary healthcare at same level as citizens"
            }
        ]
    }
}

# ---------------- UI ----------------

for domain, subdomains in data.items():
    with st.expander(f"🔵 {domain}", expanded=False):

        for subdomain, items in subdomains.items():
            st.subheader(f"🟣 {subdomain}")

            for item in items:

                st.markdown("---")

                # CARD
                with st.container():

                    st.markdown(f"### 🧾 {item['title']}")

                    col1, col2 = st.columns(2)

                    with col1:
                        st.markdown("#### 🟢 Allowed policy")
                        st.success(item["allowed"])

                    with col2:
                        st.markdown("#### 🔴 Not allowed policy")
                        st.error(item["not_allowed"])

                st.markdown("")
