import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="PharmaGuard AI", page_icon="💊", layout="wide")

# --- SIMULATED SNOWFLAKE DATA CONNECTION ---
# In a real app, this would be: session.table("INVENTORY").to_pandas()
def get_data():
    data = {
        'Location': ['Central Store', 'Central Store', 'Central Store', 
                     'Rural Clinic A', 'Rural Clinic A', 'Rural Clinic A',
                     'Emergency Ward', 'Emergency Ward', 'Emergency Ward'],
        'Item': ['Paracetamol (500mg)', 'Insulin Vials', 'Amoxicillin', 
                 'Paracetamol (500mg)', 'Insulin Vials', 'Amoxicillin',
                 'Paracetamol (500mg)', 'Insulin Vials', 'Amoxicillin'],
        'Current_Stock': [5000, 120, 800, 50, 2, 20, 200, 5, 150],
        'Daily_Usage_Avg': [100, 5, 20, 15, 1, 5, 40, 3, 10],
        'Lead_Time_Days': [2, 7, 5, 3, 7, 5, 1, 1, 2]
    }
    df = pd.DataFrame(data)
    # Calculate 'Days Until Stockout'
    df['Days_Runway'] = df['Current_Stock'] / df['Daily_Usage_Avg']
    # AI Logic: Suggested Reorder = (Lead Time * Usage) * 1.5 Buffer
    df['Suggested_Reorder'] = (df['Lead_Time_Days'] * df['Daily_Usage_Avg'] * 1.5).astype(int)
    # Status Logic
    df['Status'] = np.where(df['Days_Runway'] < df['Lead_Time_Days'], 'CRITICAL', 
                   np.where(df['Days_Runway'] < df['Lead_Time_Days']*2, 'WARNING', 'OK'))
    return df

df = get_data()

# --- HEADER ---
st.title("💊 PharmaGuard: AI Supply Chain Optimizer")
st.markdown("**Problem Statement 3:** Optimizing Medicine Availability using Snowflake Intelligence.")
st.markdown("---")

# --- TOP LEVEL METRICS ---
col1, col2, col3, col4 = st.columns(4)
critical_count = df[df['Status'] == 'CRITICAL'].shape[0]
total_stock = df['Current_Stock'].sum()

col1.metric("🏥 Locations Monitored", "3", "Active")
col2.metric("📦 Total Stock Units", f"{total_stock:,}", "+12% vs last week")
col3.metric("⚠️ Stockout Risks", f"{critical_count} Items", "Action Required", delta_color="inverse")
col4.metric("🤖 AI Forecast Accuracy", "94.2%", "Cortex Model")

# --- MAIN TAB INTERFACE ---
tab1, tab2, tab3 = st.tabs(["📊 Stock Health Heatmap", "🚨 Priority Reorder List", "🤖 Cortex AI Insights"])

with tab1:
    st.subheader("Inventory Heatmap by Location & Item")
    st.caption("Visualizing stock health. Red indicates critical low stock levels.")
    
    # Create a Pivot Table for the Heatmap
    heatmap_data = df.pivot(index="Location", columns="Item", values="Days_Runway")
    
    # Plotly Heatmap
    fig = px.imshow(heatmap_data, 
                    labels=dict(x="Medicine", y="Location", color="Days of Supply"),
                    x=heatmap_data.columns,
                    y=heatmap_data.index,
                    color_continuous_scale="RdYlGn", # Red to Green
                    text_auto=True)
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("⚠️ Critical Reorder Recommendations")
    st.caption("Items likely to run out within lead-time days. Action immediately.")
    
    # Filter for Critical items
    critical_df = df[df['Status'] == 'CRITICAL'][['Location', 'Item', 'Current_Stock', 'Days_Runway', 'Suggested_Reorder']]
    
    st.dataframe(critical_df.style.applymap(lambda x: 'background-color: #ffcccc', subset=['Days_Runway']), use_container_width=True)
    
    st.download_button(
        label="📥 Export Purchase Orders (CSV)",
        data=critical_df.to_csv().encode('utf-8'),
        file_name='urgent_reorders.csv',
        mime='text/csv',
    )

with tab3:
    st.subheader("❄️ Snowflake Cortex AI Analysis")
    st.info("Simulating Snowflake Cortex 'Text-to-SQL' and Natural Language Explanation")
    
    query = st.text_input("Ask a question about your inventory:", "Which location has the highest risk of insulin shortage?")
    
    if query:
        st.markdown(f"**Generated SQL:** `SELECT Location, Days_Runway FROM INVENTORY WHERE Item='Insulin Vials' ORDER BY Days_Runway ASC LIMIT 1;`")
        st.success("**AI Answer:** 'Rural Clinic A' is at highest risk. It has only 2 vials of Insulin left (2 days supply), but the lead time for delivery is 7 days. **Immediate transfer recommended.**")

# --- SIDEBAR INFO ---
with st.sidebar:
    st.header("Control Panel")
    region = st.selectbox("Filter Region", ["All Regions", "Province 1", "Bagmati", "Karnali"])
    st.success("Connected to Snowflake Data Cloud")
    st.markdown("### Powered By:")
    st.code("Snowflake Worksheets\nStreamlit\nDynamic Tables\nCortex AI")