import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Function to connect to Google Sheets
def connect_to_gsheet(sheet_name):
    # Define the scope
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    
    # Create credentials using the service account key
    creds = Credentials.from_service_account_file("env\secrets.json", scopes=scope)
    
    # Authorize the client
    client = gspread.authorize(creds)
    
    # Open the Google Sheet
    sheet = client.open(sheet_name).sheet1  # Access the first sheet
    return sheet

# Streamlit app
def app():
    st.title("Send Text Input to Google Sheets")

    # Text input from the user
    user_input = st.text_input("Enter some text")

    if st.button("Send to Google Sheets"):
        if user_input:
            try:
                # Connect to Google Sheets
                sheet = connect_to_gsheet("TestDrive-1")
                
                # Append the user input to the sheet
                sheet.append_row([user_input])
                
                st.success("Data sent to Google Sheets!")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter some text before submitting.")

if __name__ == "__main__":
    app()
