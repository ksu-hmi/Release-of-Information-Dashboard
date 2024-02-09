import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Production Dashboard", page_icon=":bar_chart:")

st.title("Production Dashboard - 2022")

# Read the CSV into a data frame
df = pd.read_csv("data.csv")

# Calculate the total number of releases
total_releases = df["number_done"].sum()

# Calculate the totals for each request_type
totals_by_type = df.groupby("request_type")["number_done"].sum()

# Calculate the total number of calls
total_calls = df["calls", "voicemail"].sum()

# Calculate the total pages sent
total_pages = df["pages_sent"].sum()

# Calculate images clouded and CDs created
radiology = df["cds_created", "images_clouded"].sum()

# Metrics bar
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total releases", total_releases)
col2.metric("Total calls", total_calls)
col3.metric("Total pages sent", total_pages)
col4.metric("Total images sent", radiology)

