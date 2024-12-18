import streamlit as st
import pandas as pd
import plotly.express as px

# Set the display to wide format
st.set_page_config(layout="wide")

# Load the data from the CSV file
@st.cache_data
def load_data():
    df = pd.read_csv('./data/fb.csv')
    return df

# Create the DataFrame
df = load_data()

# Create tabs
tab1, tab2 = st.tabs(["report_tab", "messages_tab"])

# Messages tab
with tab2:
    st.table(df)

# Report tab
with tab1:
    col1, col2 = st.columns(2)

    # Read and display the report
    with col1:
        report_content = open('./data/report.md').read()
        st.markdown(report_content)

    # Draw bar chart of 'Product' over 'Overall_Rating'
    with col2:
        bar_chart = px.bar(df, x='Product', y='Overall_Rating', title='Product vs Overall Rating')
        st.plotly_chart(bar_chart)

        # Draw histogram of 'Sentiment' colored by 'Product'
        histogram = px.histogram(df, x='Sentiment', color='Product', title='Sentiment Distribution by Product')
        st.plotly_chart(histogram)