# Interactive Execution Tracker using Streamlit (example)

import streamlit as st
import pandas as pd

# Set title
st.title("🚀 Training Execution Tracker – June 2025")

# Define initial data
data = {
    "Batch No": [f"Batch {i}" for i in range(1, 11)],
    "Start Date": ["2025-06-02", "2025-06-02", "2025-06-09", "2025-06-09", "2025-06-09",
                   "2025-06-12", "2025-06-13", "2025-06-16", "2025-06-16", "2025-06-18"],
    "End Date": ["2025-06-06", "2025-06-06", "2025-06-13", "2025-06-13", "2025-06-12",
                 "2025-06-17", "2025-06-18", "2025-06-20", "2025-06-20", "2025-06-20"],
    "Learners Assigned": [40]*10,
    "Trainer Name": [""]*10,
    "Status": ["Planned"]*10,
    "Attendance %": [""]*10,
    "Avg Feedback Score": [""]*10,
    "Issues/Remarks": [""]*10,
    "Next Action": [""]*10
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Editable grid
edited_df = st.data_editor(df, use_container_width=True, num_rows="dynamic")

# Save edited DataFrame
if st.button("Save Tracker Data"):
    edited_df.to_csv("execution_tracker_june2025.csv", index=False)
    st.success("✅ Tracker data saved successfully!")

# Add visualization (optional)
st.subheader("Batch Status Overview")
st.bar_chart(edited_df["Status"].value_counts())
