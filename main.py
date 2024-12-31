import streamlit as st
import csv

st.set_page_config(layout="wide")

with st.sidebar:
    st.write(":page_facing_up:  Home")
    st.write(":page_facing_up:  Contact us")

st.title("The Best Company")
content_title = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis fringilla sapien nec imperdiet. 
Nunc lacinia accumsan aliquet. Praesent sollicitudin consectetur ullamcorper. Sed semper tempor nisl, sodales elementum enim tincidunt non. 
Nullam sed felis semper justo cursus aliquet. Fusce nec commodo libero. Mauris tincidunt mauris sit amet lectus tincidunt pharetra. 
Donec ac ante justo. Proin semper ultrices ultricies. Sed condimentum laoreet urna non ornare. Proin euismod consectetur felis, ut tincidunt justo porta ullamcorper. 
Duis eu mauris mi. Suspendisse potenti. Fusce id lectus id tortor maximus hendrerit quis in lorem. Aenean mollis urna metus, at mollis lacus aliquam ac.
"""
st.write(content_title)
st.header("Our Team", divider="gray")

cols = st.columns(3)
col_index = 0

with open('data.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        with cols[col_index]:
            st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
            st.write(row['role'])
            st.image("images/" + row['image'])
            col_index += 1
            if col_index >= len(cols):
                col_index = 0
