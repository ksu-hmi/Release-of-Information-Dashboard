import streamlit as st
import sqlite3
import pandas as pd
import plotly

st.set_page_config(page_title="ROI Production", page_icon=":bar_chart:")

# Connect to the SQLite database
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Create a table to store the form data
c.execute('''CREATE TABLE IF NOT EXISTS form_data
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             date DATE,
             name TEXT,
             calls INT,
             voicemail INT,
             call_time INT,
             request_type TEXT,
             number_done INT,
             pages_sent INT,
             time_spent INT,
             cds_created INT,
             images_clouded INT,
             comment TEXT)''')
conn.commit()

# Define a function to insert data into the form_data table
def insert_data(date, name, calls, voicemail, call_time, request_type, number_done, pages_sent, time_spent, cds_created, images_clouded, comment):
    c.execute("INSERT INTO form_data (date, name, calls, voicemail, call_time, request_type, number_done, pages_sent, time_spent, cds_created, images_clouded, comment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (date, name, calls, voicemail, call_time, request_type, number_done, pages_sent, time_spent, cds_created, images_clouded, comment))
    conn.commit()

# Define a function to retrieve data from the form_data table
def get_data():
    df = pd.read_sql_query("SELECT * FROM form_data", conn)
    return df

# List of user names
user_names = [
    "Liam Patel",
    "Sophia Kim",
    "Elijah Nguyen",
    "Ava Singh",
    "Noah Rodriguez"
]

# List of release types
roi_types = [
    "Continuing care",
    "Patient",
    "Insurance",
    "Attorney",
    "Work comp",
    "Law enforcement",
    "Regulatory",
]
st.header("Production")
# Create input fields for data entry
col1, col2 = st.columns(2)

date = col1.date_input("Select date")
name = col2.selectbox("Select your name", [" ", *user_names], index=0)

col1, col2, col3 = st.columns(3)

calls = col1.number_input("Calls", help="Include both incoming and outgoing calls.", format=" %d", value=0, min_value=0)
voicemail = col2.number_input("Voicemails retrieved", format=" %d", value=0, min_value=0)
call_time = col3.number_input("Total phone time", help="Example: 1 hour 15 minutes is 1.25", format=" %d", value=0, min_value=0)

col1, col2, col3 = st.columns(3)

request_type = col1.selectbox("Type of request", [" ", *roi_types], index=0)
number_done = col2.number_input("Number of requests completed", format=" %d", value=0, min_value=0)
pages_sent = col3.number_input("Pages sent", format=" %d", value=0, min_value=0)

col1, col2, col3 = st.columns(3)

time_spent = col1.number_input("Time spent", help="Example: 1 hour 15 minutes is 1.25",format=" %d", value=0,min_value=0)
cds_created = col2.number_input("Radiology CDs created", format=" %d", value=0, min_value=0)
images_clouded = col3.number_input("Images clouded", format=" %d", value=0, min_value=0)

comment = st.text_input("Other/non productive time", help="Mail, meetings, downtime, etc.")

# Create a submit button
if st.button("Submit"):
    # Check if mandatory fields are filled
    if not (date or name or request_type):
        st.error("Please fill in all mandatory fields.")
    else:
        # Insert the input data into the form_data table
        insert_data(date, name, calls, voicemail, call_time, request_type, number_done, pages_sent, time_spent, cds_created, images_clouded, comment)
        # Show a success message
        st.success("Data submitted successfully!")
        st.experimental_rerun()

# Define a function to render the dashboard page
def render_dashboard_page():
    st.title("ROI Dashboard 2023")
    # Get the data from the form_data table
    df = get_data()
    # Show the data in a table
    st.dataframe(df)

# Define a function to render the form page
def render_form_page():
    st.write("Make sure to double check before submitting.")

# Main Streamlit app
def main():
    # Create a menu to switch between pages
    menu = ["Input production", "Dashboard"]
    choice = st.sidebar.selectbox("Select a page", menu)
    
    # Render the selected page
    if choice == "Input production":
        render_form_page()
    elif choice == "Dashboard":
        render_dashboard_page()

if __name__ == "__main__":
    main()
