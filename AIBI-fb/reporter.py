import streamlit as st
import pandas as pd
import plotly.express as px



df = pd.read_json("fb.json")

fig1 = px.histogram(df,x="Sentiment", color='Shoe', title="Customer Sentiment")

fig2 = px.histogram(df,x="Overall Rating", color='Shoe', title="Overall Rating")
fig2.update_xaxes(categoryorder='array',
                 categoryarray= ['1/5','2/5','3/5','4/5','5/5'])

with open("report.md", "r") as report_file:
    report = report_file.read()


st.set_page_config(layout="wide")

st.subheader(":blue[Customer feedback report]")
st.write("Select the report or the actual customer messages from the tabs below")

tab1, tab2 = st.tabs(["Report", "Customer messages"])

with tab1:
    col1,col2 = st.columns(2)
    with col1:      
        st.markdown(report)
    with col2:
        st.plotly_chart(fig1)
        st.plotly_chart(fig2)
with tab2:
    st.table(df)
    