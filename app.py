import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Hello World App", page_icon="🌍", layout="wide")

st.markdown("""
<style>
    .main {
        background: linear-gradient(to bottom right, #f0f2f6, #e6e9ef);
    }
    .stTitle {
        color: #1e3d59;
        font-family: 'Arial Black', sans-serif;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .custom-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

st.title("🌍 Hello World Dashboard")
st.markdown("<p style='text-align: center; color: #666; font-size: 20px;'>Welcome to an interactive Streamlit experience!</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='metric-card'><h3>Users</h3><h1>1,234</h1></div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='metric-card'><h3>Revenue</h3><h1>$45.6K</h1></div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='metric-card'><h3>Growth</h3><h1>+23%</h1></div>", unsafe_allow_html=True)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
    st.subheader("📊 Interactive Chart")
    
    df = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Sales': [120, 150, 180, 165, 190, 175],
        'Profit': [45, 65, 85, 70, 95, 80]
    })
    
    fig = px.bar(df, x='Month', y=['Sales', 'Profit'], 
                 title="Monthly Performance",
                 color_discrete_map={'Sales': '#667eea', 'Profit': '#764ba2'})
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
    st.subheader("🎯 Progress Tracking")
    
    progress_value = 75
    st.progress(progress_value)
    st.write(f"Project Completion: {progress_value}%")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    categories = ['Design', 'Development', 'Testing', 'Deployment']
    values = [90, 75, 60, 30]
    
    for cat, val in zip(categories, values):
        st.write(cat)
        st.progress(val/100)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
st.subheader("🎨 Interactive Elements")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🎉 Celebrate!", use_container_width=True):
        st.balloons()

with col2:
    if st.button("❄️ Snow Effect", use_container_width=True):
        st.snow()

with col3:
    color = st.color_picker("Pick a color", "#667eea")
    st.markdown(f"<div style='background-color: {color}; padding: 10px; border-radius: 5px; color: white; text-align: center;'>Your Color</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

with st.sidebar:
    st.title("⚙️ Settings")
    st.slider("Adjust Value", 0, 100, 50)
    st.selectbox("Choose Option", ["Option A", "Option B", "Option C"])
    st.checkbox("Enable Feature")
    
    st.markdown("---")
    st.info("This is a demo Streamlit app with custom styling and interactive visuals!")