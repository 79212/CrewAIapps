### Reporter.py ###

import streamlit as st
import pandas as pd
import plotly.express as px
 
### Set the data to be displayed in the app ###

# Read the raw customer feedback
df = pd.read_json("fb.json")

# Draw a histogram for customer sentiment 
fig_sentiment = px.histogram(df,x="Sentiment", color='Shoe', title="Customer Sentiment")

# Draw a histogram for Overall Rating
fig_rating = px.histogram(df,x="Overall Rating", color='Shoe', title="Overall Rating")
# We need to re-order the x axes ticks
fig_rating.update_xaxes(categoryorder='array',
                 categoryarray= ['1/5','2/5','3/5','4/5','5/5'])

# Read the markdown formatted report
with open("report.md", "r") as report_file:
    report = report_file.read()

### The app UI ###

st.set_page_config(layout="wide")

st.subheader(":blue[Customer feedback report]")
st.write("Select the report or the actual customer messages from the tabs below")

# Two tabs the first is the complete report and 
# the second a list of all the customer feedback messages
report_tab, customer_feedback_tab = st.tabs(["Report", "Customer messages"])

with report_tab:
    # Display the report in the left column and the figures in the right one
    report_text_col,charts_col = st.columns(2)
    with report_text_col:      
        st.markdown(report)
    with charts_col:
        st.plotly_chart(fig_sentiment)
        st.plotly_chart(fig_rating)
with customer_feedback_tab:
    # Display the complete set of messages in a table
    st.table(df)
    