import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.title("📊 Exploratory Data Analysis")
st.write("# Product Inventory Management")

# Load and display data
data = pd.read_csv("GPID.csv")
st.write("## Raw Data")
st.write(data)

# Convert date columns to datetime
data['Manufacturing Date'] = pd.to_datetime(data['Manufacturing Date'], format='%d-%m-%Y')
data['Expiration Date'] = pd.to_datetime(data['Expiration Date'], format='%d-%m-%Y')

# Univariate Analysis
st.write("## Univariate Analysis")

# Price Distribution
st.write("### Price Distribution")
bins = st.slider("Number of bins", min_value=5, max_value=100, value=30)
fig = px.histogram(data, x="Price", nbins=bins, title="Price Distribution")
st.plotly_chart(fig)

# Boxplot
st.write("### Boxplot Analysis")
fig2 = px.box(data, y="Price", title="Price Distribution Boxplot")
st.plotly_chart(fig2)

# Bivariate Analysis
st.write("## Bivariate Analysis")


# Interactive Filters
st.write("## Interactive Filters")
selected_category = st.selectbox("Select Product Category", data["Product Category"].unique())
filtered_data = data[data["Product Category"] == selected_category]

st.write(f"### Analysis for {selected_category}")
fig7 = px.scatter(filtered_data, 
                 x="Price", 
                 y="Stock Quantity",
                 color="Product Ratings",
                 title=f"Price vs Stock for {selected_category}")
st.plotly_chart(fig7)


