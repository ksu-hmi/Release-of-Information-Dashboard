import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Production Dashboard", page_icon=":bar_chart:")

st.markdown("# Production Dashboard - 2022")
st.sidebar.header("Dashboard")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)