"""Streamlit host for the This Is Math interactive instrument."""

from pathlib import Path

import streamlit as st

st.set_page_config(page_title="This Is Math", page_icon="◯", layout="wide")

instrument_path = Path(__file__).with_name("instrument.html")
st.iframe(instrument_path, width="stretch", height=920)

st.markdown(
    """
    <style>
    #MainMenu, header, footer { visibility: hidden; }
    .stApp { background: #090a0a; }
    .block-container { max-width: none; padding: 0; }
    iframe { display: block; }
    </style>
    """,
    unsafe_allow_html=True,
)
