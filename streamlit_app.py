import streamlit as st
import pandas as pd

# Load CSV file
df = pd.read_csv("conf_tourney.csv")

# Get the name of the last column
last_col = df.columns[-1]

# Convert last column to clickable links
df[last_col] = df[last_col].apply(lambda x: f'<a href="{x}" target="_blank">Link</a>')

# Title and subtitle
st.title("D1 Baseball Conference Tournament Statcast Games")
st.subheader("All times Eastern")

# Sidebar filters for each column (except the hyperlink column)
st.sidebar.header("Filter Table")

# Make a copy of the DataFrame to filter
filtered_df = df.copy()

# Apply filters to each column except the link column
for col in df.columns[:-1]:
    unique_vals = df[col].dropna().unique()
    if len(unique_vals) < 20:
        selected_vals = st.sidebar.multiselect(f"Filter by {col}:", sorted(unique_vals), default=sorted(unique_vals))
        filtered_df = filtered_df[filtered_df[col].isin(selected_vals)]
    else:
        text_filter = st.sidebar.text_input(f"Search in {col}:", "")
        if text_filter:
            filtered_df = filtered_df[filtered_df[col].astype(str).str.contains(text_filter, case=False)]

# Show the table with clickable links
st.write("Click the links to open in a new tab:")
st.write(filtered_df.to_html(escape=False, index=False), unsafe_allow_html=True)