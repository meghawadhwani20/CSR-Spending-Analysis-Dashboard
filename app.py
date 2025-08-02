import streamlit as st
import pandas as pd  # ✅ This line fixes the error
from PIL import Image

# Page configuration
st.set_page_config(page_title="CSR Insight App", layout="wide", page_icon="🌿")

# 🌿 Custom CSS for green theme + top nav bar + card UI
st.markdown("""
    <style>
    /* App background */
    .stApp {
        background-color: #dcedc8 !important;
    }

    /* Hide the sidebar */
    section[data-testid="stSidebar"] {
        display: none !important;
    }

    /* Card style */
    .card {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 25px;
        margin: 10px 0;
        box-shadow: 0 6px 12px rgba(0, 128, 0, 0.1);
    }

    /* Top nav buttons */
    .nav-buttons {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-top: 10px;
        margin-bottom: 30px;
    }

    .nav-buttons button {
        background-color: #aed581;
        border: none;
        border-radius: 10px;
        padding: 10px 25px;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .nav-buttons button:hover {
        background-color: #9ccc65;
    }
    </style>
""", unsafe_allow_html=True)

# --------------------------- TOP NAVIGATION ---------------------------
st.markdown('<div class="nav-buttons">', unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("🏠 Home"):
        st.session_state.page = "Home"
with col2:
    if st.button("📊 Dashboard"):
        st.session_state.page = "Dashboard"
with col3:
    if st.button("🧰 Filter Tool"):
        st.session_state.page = "Filter Tool"
with col4:
    if st.button("🏆 Recommendations"):
        st.session_state.page = "Recommendations"
with col5:
    if st.button("📞 Contact"):
        st.session_state.page = "Contact"

st.markdown('</div>', unsafe_allow_html=True)

# --------------------------- PAGE STATE ---------------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

page = st.session_state.page

# --------------------------- HOME ---------------------------
if page == "Home":
    st.markdown("<h1 style='text-align: center;'>🌿 CSR Insight & Strategy</h1>", unsafe_allow_html=True)

# CSR Banner Image
    st.image("https://candourlegal.com/wp-content/uploads/2024/06/CORPORATE-SOCIAL-RESPONSIBILITY-CRITICAL-ANALYSIS-1.jpg", use_container_width=True)

    st.markdown("Explore CSR trends, top companies, and funding opportunities using this dashboard.")
        # ---------------- What This App Includes ----------------
        # What this app includes
    st.markdown("## 🔍 What this app includes")
    st.markdown("#### Comprehensive tools for CSR analysis and outreach")

    # Row 1
    row1_col1, row1_col2 = st.columns(2)

    with row1_col1:
        st.markdown("""
            <div class="card">
                <h5>📊 CSR trends</h5>
                <p>Comprehensive analytics of CSR spending patterns across 200+ companies</p>
            </div>
        """, unsafe_allow_html=True)

    with row1_col2:
        st.markdown("""
            <div class="card">
                <h5>🔍 Filter tool</h5>
                <p>Advanced filtering by sector, company type, and compliance status</p>
            </div>
        """, unsafe_allow_html=True)

    # Row 2
    row2_col1, row2_col2 = st.columns(2)

    with row2_col1:
        st.markdown("""
            <div class="card">
                <h5>🏆 Smart outreach recommendations</h5>
                <p>AI-powered insights to identify the best partnership opportunities</p>
            </div>
        """, unsafe_allow_html=True)

    with row2_col2:
        st.markdown("""
            <div class="card">
                <h5>📩 Contact form</h5>
                <p>Direct connection facilitation with target companies</p>
            </div>
        """, unsafe_allow_html=True)

    # Highlight metrics row
    col3, col4, col5, col6 = st.columns(4)
    col3.metric("📈 Companies Analyzed", "200+")
    col4.metric("💰 Total CSR Budget", "₹222.93 Cr")
    col5.metric("✅ Compliance Rate", "21.5%")
    col6.metric("📬 Outreach Opportunities", "70")



# --------------------------- DASHBOARD ---------------------------
elif page == "Dashboard":
    st.title("📊 CSR Dashboard")
    st.image("C:/Users/Infinity/OneDrive/Desktop/Internship/CSR/Csr_app/dashboard.png", use_container_width=True)
    st.caption("Snapshot from Power BI dashboard")

        # Highlight metric cards under Dashboard image
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
            <div class="card">
                <h5>Total Companies</h5>
                <h3 style='color:#2e7d32;'>200+</h3>
                <p>Analyzed companies</p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="card">
                <h5>CSR Compliance</h5>
                <h3 style='color:#2e7d32;'>21.5%</h3>
                <p>Meeting requirements</p>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="card">
                <h5>Total CSR Spend</h5>
                <h3 style='color:#2e7d32;'>₹222.93 Cr</h3>
                <p>This fiscal year</p>
            </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
            <div class="card">
                <h5>NGO Opportunities</h5>
                <h3 style='color:#2e7d32;'>70</h3>
                <p>Active outreach targets</p>
            </div>
        """, unsafe_allow_html=True)
    st.markdown("""
        <style>
        .card {
            background-color: #f4fdf7;
            padding: 20px 25px;
            border-radius: 12px;
            border: 1px solid #cde9d7;
            margin-top: 20px;
        }
        .card h4 {
            color: #1b5e20;
            margin-bottom: 10px;
        }
        .card p {
            color: #333;
            font-size: 15px;
            margin: 8px 0;
        }
        </style>

        <div class="card">
        <h4>📌 Key Insights</h4>
        <p> ✔️Pharmaceuticals and FMCG sectors lead in number of companies, ideal for large-scale CSR engagement.</p>
        <p>✔️Retail sector shows the highest average CSR spend, making it a top priority for outreach.</p>
        <p>✔️Only 21.5% companies are CSR compliant — signaling major gaps in policy adoption.</p>
        <p>✔️Over 75% companies fall into non-compliant category despite many having significant budgets.</p>
        <p>✔️Indian firms dominate (69.5%), making them the primary focus for localized initiatives.</p>
        <p>✔️Low and High funding categories cover the majority — outreach plans should align accordingly.</p>
        
        </div>
            """, unsafe_allow_html=True)



# --------------------------- FILTER TOOL ---------------------------
elif page == "Filter Tool":
    st.title("🔍 Company Filter Tool")
    df = pd.read_excel(r"C:/Users/Infinity/OneDrive/Desktop/Internship/CSR/Csr_app/final_csr_data.xlsx")

    col1, col2 = st.columns(2)
    with col1:
        sector = st.multiselect("Select Sector", sorted(df["Sector"].dropna().unique()))
        compliance = st.multiselect("Compliance Status", sorted(df["Compliance"].dropna().unique()))
    with col2:
        origin = st.multiselect("Company_Type (Indian/Foreign)", sorted(df["Company_Type"].dropna().unique()))
        funding = st.multiselect("Funding Category", sorted(df["Funding_Category"].dropna().unique()))

    filtered_df = df.copy()
    if sector:
        filtered_df = filtered_df[filtered_df["Sector"].isin(sector)]
    if origin:
        filtered_df = filtered_df[filtered_df["Company_Type"].isin(origin)]
    if compliance:
        filtered_df = filtered_df[filtered_df["Compliance"].isin(compliance)]
    if funding:
        filtered_df = filtered_df[filtered_df["Funding_Category"].isin(funding)]

    st.success(f"{len(filtered_df)} companies match your filters.")
    st.dataframe(filtered_df)


# --------------------------- RECOMMENDATIONS ---------------------------
elif page == "Recommendations":
    st.title(" Recommended Companies")

    recs = [
        {"name": "Dr. Reddy’s Laboratories", "note": "Active in Pharmaceuticals, ideal for health-related outreach"},
        {"name": "Wipro Ltd", "note": "Known for strong education initiatives, major CSR contributor"},
        {"name": "Cipla Ltd", "note": "Focused on healthcare with significant CSR spending"},
        {"name": "Infosys Ltd", "note": "High impact in education sector with consistent CSR presence"},
    ]

    for rec in recs:
        st.markdown(f"✅ **{rec['name']}** — {rec['note']}")

    st.markdown("""
    <div style="border: 1px solid #c8e6c9; border-radius: 10px; background-color: #e8f5e9; padding: 15px; margin-bottom: 20px;">
        <div style="border: 1px solid #c8e6c9; border-radius: 10px; background-color: #e8f5e9; padding: 15px; margin-bottom: 20px;">
  <b>⚠️ Key Insight:</b> NGOs should focus more on <b>Pharmaceuticals</b> and <b>FMCG</b> sectors, and reach out to companies like <b>Dr. Reddy’s Laboratories</b> and <b>ITC Ltd</b> who have high CSR budgets but limited direct NGO engagement.
</div>

    """, unsafe_allow_html=True)

    st.markdown("""
    ### 🔻 Top Sectors with Non-Compliance
    <p style='color: grey; font-size: 14px;'>Priority sectors where NGOs can make the most impact</p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div style="border:1px solid #ddd; border-radius:10px; padding:15px; margin-bottom:15px;">
            <h5>Pharmaceuticals <span style='background:#f44336;color:white;padding:3px 8px;border-radius:10px;font-size:12px;'>5.26% Compliant</span></h5>
            <p>Companies: <b>19</b></p>
            <p>Avg CSR: <b>₹131.9K</b></p>
        </div>

        <div style="border:1px solid #ddd; border-radius:10px; padding:15px;">
            <h5>FMCG <span style='background:#f44336;color:white;padding:3px 8px;border-radius:10px;font-size:12px;'>29.41% Compliant</span></h5>
            <p>Companies: <b>17</b></p>
            <p>Avg CSR: <b>₹44.46K</b></p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="border:1px solid #ddd; border-radius:10px; padding:15px; margin-bottom:15px;">
            <h5>Energy <span style='background:#f44336;color:white;padding:3px 8px;border-radius:10px;font-size:12px;'>23.08% Compliant</span></h5>
            <p>Companies: <b>13</b></p>
            <p>Avg CSR: <b>₹1228.9K</b></p>
        </div>

        <div style="border:1px solid #ddd; border-radius:10px; padding:15px;">
            <h5>IT Services <span style='background:#f44336;color:white;padding:3px 8px;border-radius:10px;font-size:12px;'>30.77% Compliant</span></h5>
            <p>Companies: <b>13</b></p>
            <p>Avg CSR: <b>₹711.1K</b></p>
        </div>
        """, unsafe_allow_html=True)

    # 🔻🔻🔻 ADDING LAST IMAGE-LIKE DESIGN CARD 🔻🔻🔻
    st.markdown("""
<div style="border: 1px solid #dcecdc; border-radius: 12px; padding: 25px; background-color: #f9fdf9;">
  <h4 style="margin-bottom: 5px; color: #1b5e20;">📈 High CSR Budget</h4>
  <p style="color: #666; font-size: 14px;">Companies with significant CSR budgets </p>

  <div style="border: 1px solid #e0e0e0; border-radius: 10px; padding: 15px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <div style="font-weight: bold;">Flipkart India</div>
      <div style="color: gray; font-size: 14px;">Retail</div>
    </div>
    <div style="text-align: right;">
      <div style="color: #2e7d32; font-size: 18px; font-weight: bold;">₹1,48,450 Cr</div>
      <div style="background-color: #2e7d32; color: white; font-size: 12px; padding: 2px 8px; border-radius: 8px;">Indian</div>
    </div>
  </div>

  <div style="border: 1px solid #e0e0e0; border-radius: 10px; padding: 15px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <div style="font-weight: bold;">Eni S.p.A. </div>
      <div style="color: gray; font-size: 14px;">Oil & Gas </div>
    </div>
    <div style="text-align: right;">
      <div style="color: #2e7d32; font-size: 18px; font-weight: bold;">₹12,900 Cr </div>
      <div style="background-color: #2e7d32; color: white; font-size: 12px; padding: 2px 8px; border-radius: 8px;">Foreign</div>
    </div>
  </div>

  <div style="border: 1px solid #e0e0e0; border-radius: 10px; padding: 15px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <div style="font-weight: bold;">Enel Green Power</div>
      <div style="color: gray; font-size: 14px;">Energy</div>
    </div>
    <div style="text-align: right;">
      <div style="color: #2e7d32; font-size: 18px; font-weight: bold;">₹9,700 Cr</div>
      <div style="background-color: #2e7d32; color: white; font-size: 12px; padding: 2px 8px; border-radius: 8px;">Foreign</div>
    </div>
  </div>

  <div style="border: 1px solid #e0e0e0; border-radius: 10px; padding: 15px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <div style="font-weight: bold;">Accenture plc</div>
      <div style="color: gray; font-size: 14px;">IT Services</div>
    </div>
    <div style="text-align: right;">
      <div style="color: #2e7d32; font-size: 18px; font-weight: bold;">₹4,150 Cr</div>
      <div style="background-color: #2e7d32; color: white; font-size: 12px; padding: 2px 8px; border-radius: 8px;">Foreign</div>
    </div>
  </div>
</div>

""", unsafe_allow_html=True)
    st.markdown("""
<div style="border: 1px solid #dcecdc; border-radius: 12px; padding: 25px; background-color: #f9fdf9;">
  <h4 style="margin-bottom: 5px; color: #1b5e20;">📋 Sector-wise Compliance Overview</h4>
  <p style="color: #666; font-size: 14px;">Complete breakdown of compliance rates across all sectors</p>

  <table style="width:100%; border-collapse: collapse; margin-top: 10px;">
    <thead style="background-color: #fafafa;">
      <tr>
        <th style="text-align: left; padding: 10px;">Sector</th>
        <th style="text-align: left; padding: 10px;">Total Companies</th>
        <th style="text-align: left; padding: 10px;">Compliant</th>
        <th style="text-align: left; padding: 10px;">Non-Compliant</th>
        <th style="text-align: left; padding: 10px;">Compliance Rate</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding: 10px;">IT Services</td>
        <td>13</td>
        <td>🟢 30.8%</td>
        <td>🔴 69.2%</td>
        <td><span style="background-color: #d32f2f; color: white; padding: 4px 10px; border-radius: 10px;">Poor</span></td>
      </tr>
      <tr>
        <td style="padding: 10px;">Banking</td>
        <td>7</td>
        <td>🟢 42.9%</td>
        <td>🔴 51.7%</td>
        <td><span style="background-color: #d32f2f; color: white; padding: 4px 10px; border-radius: 10px;">Poor</span></td>
      </tr>
      <tr>
        <td style="padding: 10px;">Oil & Gas</td>
        <td>11</td>
        <td>🟢 45.5%</td>
        <td>🔴 54.5%</td>
        <td><span style="background-color: #d32f2f; color: white; padding: 4px 10px; border-radius: 10px;">Poor</span></td>
      </tr>
      <tr>
        <td style="padding: 10px;">Telecom</td>
        <td>7</td>
        <td>🟢 37.5%</td>
        <td>🔴 62.5%</td>
        <td><span style="background-color: #d32f2f; color: white; padding: 4px 10px; border-radius: 10px;">Poor</span></td>
      </tr>
      <tr>
        <td style="padding: 10px;">FMCG</td>
        <td>17</td>
        <td>🟢 29.4%</td>
        <td>🔴 70.6%</td>
        <td><span style="background-color: #2e7d32; color: white; padding: 4px 10px; border-radius: 10px;">Good</span></td>
      </tr>
      <tr>
        <td style="padding: 10px;">Aviation</td>
        <td>6</td>
        <td>🟢 33.3%</td>
        <td>🔴 66.7%</td>
        <td><span style="background-color: #2e7d32; color: white; padding: 4px 10px; border-radius: 10px;">Good</span></td>
      </tr>
    </tbody>
  </table>
</div>
""", unsafe_allow_html=True)
    st.markdown("""
                        <style>
                        .card {
                            background-color: #f4fdf7;
                            padding: 20px 25px;
                            border-radius: 12px;
                            border: 1px solid #cde9d7;
                            margin-top: 20px;
                        }
                        .card h4 {
                            color: #1b5e20;
                            margin-bottom: 10px;
                        }
                        .card p {
                            color: #333;
                            font-size: 15px;
                            margin: 8px 0;
                        }
                        </style>

                        <div class="card">
                        <h4>📌 Key Insights</h4>
                        <p>✔️ Low Compliance Rate: Only 21.5% of all companies follow CSR norms.</p>
                        <p>✔️ Foreign Companies Dominate CSR Budget: Majority CSR contributions come from foreign firms.</p>
                        <p>✔️ Top Sectors With Issues: Pharma, FMCG, Energy, IT have the highest non-compliance.</p>
                        <p>✔️ 100% Contact Reachability: All companies have email or phone listed – outreach is feasible.</p>
                        <p>✔️ Retail Sector shows the highest average CSR per company (~₹20,000+), indicating high impact potential.</p>
                        <p>✔️ Banking sector leads with 92% compliance, while E-commerce lags at 25%.</p>
                        <p>✔️ Over 50 companies fall into the "non-compliant but high CSR budget" category.</p>
                        <p>✔️ Manufacturing offers mid-tier compliance with partnership potential.</p>
                        </div>

                        <div class="card">
                        <h4>🎯 Recommendations</h4>
                        <p>📬 <b>Focus outreach on 157 non-compliant companies</b> — especially in Pharmaceuticals, FMCG, IT, and Energy, where compliance is low but CSR budgets are high.</p>

                        <p>📞 <b>Leverage 100% contact availability</b> — all 200 companies have valid contact details, making it feasible to reach out for healthcare and education partnerships.</p>

                        <p>📊 <b>Target sectors like Retail and Energy</b> with high CSR spending (~₹20K+ per company) but low compliance — these are high-potential engagement areas.</p>

                        <p>🇮🇳 <b>Encourage Indian companies</b> (69.5% of dataset) to improve CSR contributions, as they currently contribute less compared to foreign firms.</p>

                        <p>🏆 <b>Showcase success stories from Banking and Apparel sectors</b> (with 90%+ compliance) to inspire underperforming sectors like E-commerce (25%) and FMCG.</p>

                        """, unsafe_allow_html=True)





# --------------------------- CONTACT FORM ---------------------------
elif page == "Contact":
    st.title("📨 CSR Outreach Interest Form")
    st.markdown("Please fill out the form below to express interest in collaborating on CSR initiatives.")

    with st.form("csr_form", clear_on_submit=True):
        # Auto-filled company name (from a list)
        companies = ["Tata Steel", "Infosys", "Biocon", "ITC", "Wipro"]
        company_name = st.selectbox("Company Name", companies)

        csr_head = st.text_input("CSR Head Name")
        contact_email = st.text_input("Contact Email")

        focus_areas = st.multiselect(
            "CSR Focus Areas",
            ["Education", "Health"]
        )

        budget_range = st.selectbox(
            "Budget Range",
            ["< ₹1 Cr", "₹1-5 Cr", "₹5+ Cr"]
        )

        

        location_pref = st.radio(
            "Location Preference",
            ["Pan India", "Region-specific"]
        )

        contact_date = st.date_input("📅 Preferred Contact Date")

        notes = st.text_area("Additional Notes (Optional)")

        agree = st.checkbox("✅ I agree to share my details for CSR outreach.")

        submit = st.form_submit_button("Submit")

    if submit:
        if not agree:
            st.warning("☝️ Please agree to share your details before submitting.")
        elif not contact_email or not csr_head:
            st.error("Please fill in all required fields (CSR Head and Contact Email).")
        else:
            st.success("✅ Thank you! Your interest has been recorded.")
            # Optional: Save to Google Sheet, database, or email backend

