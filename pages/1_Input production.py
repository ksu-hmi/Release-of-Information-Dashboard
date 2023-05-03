import streamlit as st
import pandas as pd
import os

if "csv_written" not in st.session_state:
    st.session_state.csv_written = False
    
# Define function to save data
def save_data(date, name, calls, voicemail, call_time, request_type, number_done, pages_sent, time_spent, cds_created, images_clouded, comment):
    data = {
        'date': [date],
        'name': [name],
        'calls': [calls],
        'voicemail': [voicemail],
        'call_time': [call_time],
        'request_type': [request_type],
        'number_done': [number_done],
        'pages_sent': [pages_sent],
        'time_spent': [time_spent],
        'cds_created': [cds_created],
        'images_clouded': [images_clouded],
        'comment': [comment]
    }
    df = pd.DataFrame(data)
    
    # Check if CSV file already exists
    if os.path.exists('data.csv'):
        # Append data to existing file without header
        df.to_csv('data.csv', mode='a', index=False, header=False)
    else:
        # Write headers and data to new file
        df.to_csv('data.csv', mode='a', index=False, header=True)

    # Set a session state variable to True to avoid writing header row again
    st.session_state.csv_written = True

# Define function to read data from CSV file
def get_data():
    if not os.path.exists('data.csv'):
        return pd.DataFrame()

    return pd.read_csv('data.csv')

# List of user names
user_names = [
    "Liam Patel",
    "Sophia Kim",
    "Elijah Nguyen",
    "Ava Singh",
    "Noah Rodriguez",
    "Karen Smith", 
    "James McCarty"
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

st.set_page_config(page_title="Input production", page_icon=":lower_left_fountain_pen:")

st.markdown("# Production Input")
st.sidebar.header("Production input")
st.write(
    "Please enter your production as accurately as possible. Double check before hitting submit."
)

col1, col2 = st.columns(2)

date = col1.date_input("Select date")
name = col2.selectbox("Select your name", [" ", *user_names], index=0)

col1, col2, col3 = st.columns(3)

calls = col1.number_input("Calls", help="Include both incoming and outgoing calls.", value=0, min_value=0)
voicemail = col2.number_input("Voicemails retrieved", format=" %d", value=0, min_value=0)
call_time = col3.number_input("Total phone time", help="Example: 1 hour 15 minutes is 1.25", value=0, min_value=0)

col1, col2, col3 = st.columns(3)

request_type = col1.selectbox("Type of request", [" ", *roi_types], index=0)
number_done = col2.number_input("Number of requests completed", value=0, min_value=0)
pages_sent = col3.number_input("Pages sent", value=0, min_value=0)

col1, col2, col3 = st.columns(3)

time_spent = col1.number_input("Time spent", help="Example: 1 hour 15 minutes is 1.25", value=0, min_value=0)
cds_created = col2.number_input("Radiology CDs created", value=0, min_value=0)
images_clouded = col3.number_input("Images clouded", value=0, min_value=0)

comment = st.text_input("Other/non productive time", help="Mail, meetings, downtime, etc.")

# Create a submit button
if st.button("Submit"):
     # Check if mandatory fields are filled
    if not (date and name and request_type):
        st.error("Please fill in all mandatory fields.")
    else:
        # Insert the input data into the form_data table
        save_data(date, name, calls, voicemail, call_time, request_type, number_done, pages_sent, time_spent, cds_created, images_clouded, comment)
        # Show a success message
        st.success("Data submitted successfully!")
        st.experimental_rerun()
