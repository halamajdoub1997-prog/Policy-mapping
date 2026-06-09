import streamlit as st

st.title("HIV Continuum of Care for Migrants")

data = {
    "Primary Prevention": {
        "PrEP Access": [
            {
                "indicator": "PrEP access (Migrants)",
                "yes": "Migrants can access PrEP at same level as citizens",
                "no": "Migrants cannot access PrEP at same level as citizens"
            }
        ]
    }
}

for domain, subdomains in data.items():
    with st.expander(domain):
        for subdomain, indicators in subdomains.items():
            st.subheader(subdomain)

            for item in indicators:
                st.markdown(f"### {item['indicator']}")
                col1, col2 = st.columns(2)

                with col1:
                    st.success("YES")
                    st.write(item["yes"])

                with col2:
                    st.error("NO")
                    st.write(item["no"])
