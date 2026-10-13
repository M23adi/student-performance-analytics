import streamlit as st
import pandas as pd
import numpy as np
from functions import (
    load_data, calculate_total, calculate_average,
    assign_grades, determine_pass_fail, get_class_summary,
    subject_wise_analysis, top_performers, department_summary,
    SUBJECT_COLS,
)

st.set_page_config(page_title="Student Performance Analytics", layout="wide")
st.title("Student Performance Analytics System")
st.caption("By Aditya Medhane | Python with AI - EWB Courses")

df = pd.read_csv("students.csv")
df = calculate_total(df)
df = calculate_average(df)
df = assign_grades(df)
df = determine_pass_fail(df)

summary = get_class_summary(df)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Class Average", summary["Class Average"])
col2.metric("Pass Rate", f"{round(summary['Passed']/summary['Total Students']*100,1)}%")
col3.metric("Highest Avg", summary["Highest Average"])
col4.metric("Total Students", summary["Total Students"])

st.divider()

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Student Data", "Subject Analysis", "Top Performers",
    "Department Summary", "Pass/Fail Details"
])

with tab1:
    st.subheader("All Students")
    show_cols = ["Student_ID", "Name", "Department", "Total", "Average", "Grade", "Status"]
    st.dataframe(df[show_cols], use_container_width=True, hide_index=True)

with tab2:
    st.subheader("Subject-Wise Performance")
    subj_df = subject_wise_analysis(df)
    st.dataframe(subj_df, use_container_width=True, hide_index=True)
    st.bar_chart(subj_df.set_index("Subject")["Average"])

with tab3:
    st.subheader("Top 5 Students")
    top = top_performers(df, n=5)
    st.dataframe(top, use_container_width=True, hide_index=True)

with tab4:
    st.subheader("Department-Wise Comparison")
    dept_df = department_summary(df).reset_index()
    st.dataframe(dept_df, use_container_width=True, hide_index=True)

with tab5:
    st.subheader("Pass / Fail Breakdown")
    c1, c2 = st.columns(2)
    c1.metric("Passed", summary["Passed"])
    c2.metric("Failed", summary["Failed"])
    failed = df[df["Status"] == "Fail"]
    if len(failed) > 0:
        st.write("Students who failed:")
        st.dataframe(failed[["Student_ID", "Name", "Average", "Attendance"]],
                     use_container_width=True, hide_index=True)

st.divider()

st.subheader("Grade Distribution")
grade_counts = df["Grade"].value_counts().sort_index()
st.bar_chart(grade_counts)
