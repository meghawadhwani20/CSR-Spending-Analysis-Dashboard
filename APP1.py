import streamlit as st
import pandas as pd

st.set_page_config(page_title="CSR Insight App", layout="wide", page_icon="🌿")

# --------- Initialize Navigation ---------
if "page" not in st.session_state:
    st.session_state.page = "Home"

# --------- Navigation Button Click Handlers ---------
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("🏠 Home"):
        st.session_state.page = "Home"
with col2:
    if st.button("📊 Dashboard"):
        st.session_state.page = "Dashboard"
with col3:
    if st.button("🔍 Filter Tool"):
        st.session_state.page = "Filter Tool"
with col4:
    if st.button("📩 Contact"):
        st.session_state.page = "Contact"

# --------- CSS to Overlap Buttons ---------
st.markdown("""
    <style>
    .stButton > button {
        background-color: #2e7d32;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 8px;
        margin-top: -70px;
        z-index: 9999;
    }
    .stButton > button:hover {
        background-color: #1b5e20;
    }
    </style>
""", unsafe_allow_html=True)

# --------- Banner Image with Buttons Overlapping ---------
st.image("https://candourlegal.com/wp-content/uploads/2024/06/CORPORATE-SOCIAL-RESPONSIBILITY-CRITICAL-ANALYSIS-1.jpg", use_container_width=True)

# --------- PAGE CONTENTS ---------
if st.session_state.page == "Home":
    st.title("🌿 CSR Insight & Strategy")
    st.markdown("Welcome to the CSR Dashboard. Use the tools above to navigate.")

elif st.session_state.page == "Dashboard":
    st.title("📊 Dashboard")
    st.image("https://i.imgur.com/nDnM6Rc.png", use_container_width=True)
    st.markdown("This is where your Power BI dashboard image or iframe can go.")

elif st.session_state.page == "Filter Tool":
    st.title("🔍 Filter Tool")
    try:
        df = pd.read_excel("final_csr_data.xlsx")
    except:
        df = pd.DataFrame({
            "Sector": ["IT", "Banking"],
            "Compliance": ["Yes", "No"],
            "Company_Type": ["Indian", "Foreign"],
            "Funding_Category": ["High", "Low"]
        })

    sector = st.multiselect("Sector", df["Sector"].unique())
    compliance = st.multiselect("Compliance", df["Compliance"].unique())

    filtered = df.copy()
    if sector:
        filtered = filtered[filtered["Sector"].isin(sector)]
    if compliance:
        filtered = filtered[filtered["Compliance"].isin(compliance)]

    st.dataframe(filtered)

elif st.session_state.page == "Contact":
    st.title("📩 Contact")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Send")
        if submit:
            st.success("Thank you! We'll get in touch.")

