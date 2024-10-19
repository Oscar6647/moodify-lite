import streamlit as st
import pandas as pd
import numpy as np

# streamlit_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.set_page_config(
    page_title="sub-test READ DATA!",
    page_icon="👋",
)

st.write("# Connect (Read) to Sheets!")

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet="https://docs.google.com/spreadsheets/d/18GNjdOm-2nqpbRnVAOPH2Xk0ULcZCTO4t6ozE5U4Zzo/edit?gid=0", usecols=[0, 1])
st.dataframe(data)

