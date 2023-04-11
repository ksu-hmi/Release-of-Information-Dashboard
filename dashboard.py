import streamlit as st
import sqlite3
import pandas as pd
import plotly
 
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
    c.execute("INSERT INTO form_data (date, name, calls, voicemail, call_time, request_type, number_done, pages_sent, time_spent, cds_created, images_clouded, comment VALUES (?, ?, ?)", (date, name, calls, voicemail, call_time, request_type, number_done, pages_sent, time_spent, cds_created, images_clouded, comment))
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
# Define a function to render the form page
def render_form_page():
    st.title("Production Form")
    # Create input fields for data entry
    date = st.date_input("Select date")
    name = st.selectbox("Select your name", user_names)
    calls = st.number_input("Calls - incoming and outgoing")
    voicemail = st.number_input("Voicemails retreived")
    call_time = st.number_input("Total phone time")
    request_type = st.selectbox("Type of request", roi_types)
    number_done = st.number_input("Number of requests completed")
    pages_sent = st.number_input("Pages sent")
    time_spent = st.number_input("Time spent (example 1 hour 15 minutes is 1.25)")
    cds_created = st.number_input("Radiology CDs created")
    images_clouded = st.number_input("Images clouded")
    comment = st.text_input("Other/non productive time")

    # Display the data entered by the user
    st.subheader("Please double-check your entries:")
    st.write("Date:", date)
    st.write("Name:", name)
    st.write("Calls:", calls)
    st.write("Voicemail:", voicemail)
    st.write("Call time:", call_time)
    st.write("Request type:", request_type)
    st.write("Number of requests completed:", number_done)
    st.write("Pages sent:", pages_sent)
    st.write("Time spent:", time_spent)
    st.write("Radiology CDs created:", cds_created)
    st.write("Images clouded:", images_clouded)
    st.write("Other/non-productive time:", comment)

    # Create a submit button
    if st.button("Submit"):
        # Insert the input data into the form_data table
        insert_data(date, name, calls, voicemail, call_time, request_type, number_done, pages_sent, time_spent, cds_created, images_clouded, comment)
        # Show a success message
        st.success("Data submitted successfully!")
 
     # Add a button to enter more data
    if st.button("Enter additional data"):
        # Clear the input fields
        st.experimental_rerun()

# Define a function to render the dashboard page
def render_dashboard_page():
    st.title("ROI Dashboard 2023")
    # Get the data from the form_data table
    df = get_data()
    # Show the data in a table
    st.dataframe(df)
 
# Main Streamlit app
def main():
    st.set_page_config(page_title="ROI Production", page_icon=":bar_chart:")
    # Create a menu to switch between pages
    menu = ["Form Page", "Dashboard Page"]
    choice = st.sidebar.selectbox("Select a page", menu)
    # Render the selected page
    if choice == "Form Page":
        render_form_page()
    elif choice == "Dashboard Page":
        render_dashboard_page()
 
if __name__ == "__main__":
    main()
