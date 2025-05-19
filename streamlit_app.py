import streamlit as st
import pandas as pd

# Load CSV file
df = pd.read_csv("conf_tourney.csv")

# Get the name of the last column
last_col = df.columns[-1]

# Convert last column to clickable links
df[last_col] = df[last_col].apply(lambda x: f'<a href="{x}" target="_blank">Link</a>')

# Page title and subtitle
st.title("D1 Baseball Conference Tournament Statcast Games")
st.subheader("All times Eastern")

# Optional: filter across all columns with a search box
search = st.text_input("Search all columns:")

# Apply search filter
if search:
    df_filtered = df[df.apply(lambda row: row.astype(str).str.contains(search, case=False).any(), axis=1)]
else:
    df_filtered = df

# Display the DataFrame with hyperlinks
st.write("Click the links to open in a new tab:")
st.write(df_filtered.to_html(escape=False, index=False), unsafe_allow_html=True)