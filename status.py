import streamlit as st
import time

# Create a progress bar object with a label and a custom color
progress_bar = st.progress(0, text="test")
progress_text = st.empty()
progress_bar.color = 'orange'
progress_bar.progress(0)

# Update the progress bar as your program runs
for i in range(100):
    time.sleep(0.1) # Simulate a long-running process
    progress_bar.progress(i+1)
    progress_text.text(f"Processing: {i+1}%")
