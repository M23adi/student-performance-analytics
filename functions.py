"""
functions.py
------------
This file contains all the helper functions used in the Student Performance
Analytics System. Keeping them separate from main.py makes the code easier
to read, test, and maintain.

Author  : Medha
Date    : October 2026
Course  : Python with AI – EWB Courses
"""

import numpy as np
import pandas as pd


# ---------- column helpers ----------

# These are the five subject columns present in the dataset.
SUBJECT_COLS = ["Math", "Science", "English", "Computer", "History"]


def load_data(filepath):
    """
    Read the CSV file and return it as a Pandas DataFrame.
    Prints a short summary so the user knows data was loaded properly.
    """
    df = pd.read_csv(filepath)
    print(f"Dataset loaded successfully - {len(df)} records found.\n")
    return df


# ---------- per-student calculations ----------

def calculate_total(df):
    """Add a 'Total' column that is the sum of all five subject marks."""
    df["Total"] = df[SUBJECT_COLS].sum(axis=1)
    return df


def calculate_average(df):
    """Add an 'Average' column (mean of the five subjects, rounded to 2 decimals)."""
    df["Average"] = df[SUBJECT_COLS].mean(axis=1).round(2)
    return df


def assign_grade(avg):
    """
    Return a letter grade for a given average value.

    Grading scale used:
        90 and above  -> A+
        80 – 89       -> A
        70 – 79       -> B
        60 – 69       -> C
        50 – 59       -> D
        Below 50      -> F
    """
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


def assign_grades(df):
    """Apply the grading function to every student and store it in a 'Grade' column."""
    df["Grade"] = df["Average"].apply(assign_grade)
    return df


def determine_pass_fail(df, passing_avg=50, min_attendance=60):
    """
    A student passes if:
      1. Their average marks are >= passing_avg  (default 50)
      2. Their attendance is >= min_attendance %  (default 60)

    Adds a 'Status' column with "Pass" or "Fail".
    """
    conditions = (df["Average"] >= passing_avg) & (df["Attendance"] >= min_attendance)
    df["Status"] = np.where(conditions, "Pass", "Fail")
    return df


# ---------- aggregate / class-level analysis ----------

def get_class_summary(df):
    """
    Return a dictionary with overall class-level statistics computed
    using NumPy for the numerical heavy-lifting.
    """
    averages = np.array(df["Average"])
    summary = {
        "Class Average": round(np.mean(averages), 2),
        "Highest Average": round(np.max(averages), 2),
        "Lowest Average": round(np.min(averages), 2),
        "Std Deviation": round(np.std(averages), 2),
        "Total Students": len(df),
        "Passed": int((df["Status"] == "Pass").sum()),
        "Failed": int((df["Status"] == "Fail").sum()),
    }
    return summary


def subject_wise_analysis(df):
    """
    For each subject, compute mean, max and min marks.
    Returns a new DataFrame that summarises subject performance.
    """
    records = []
    for subj in SUBJECT_COLS:
        marks = np.array(df[subj])
        records.append({
            "Subject": subj,
            "Average": round(np.mean(marks), 2),
            "Highest": int(np.max(marks)),
            "Lowest": int(np.min(marks)),
        })

    analysis_df = pd.DataFrame(records)
    return analysis_df


def top_performers(df, n=5):
    """Return the top-n students sorted by their average marks (descending)."""
    top = df.nlargest(n, "Average")[["Student_ID", "Name", "Department", "Average", "Grade"]]
    return top.reset_index(drop=True)


def department_summary(df):
    """
    Group students by department and show the mean average and pass rate
    for each one. Useful for comparing department-level performance.
    """
    dept_stats = df.groupby("Department").agg(
        Students=("Student_ID", "count"),
        Dept_Average=("Average", "mean"),
        Pass_Count=("Status", lambda x: (x == "Pass").sum()),
    )
    dept_stats["Dept_Average"] = dept_stats["Dept_Average"].round(2)
    dept_stats["Pass_Rate(%)"] = ((dept_stats["Pass_Count"] / dept_stats["Students"]) * 100).round(1)
    return dept_stats


def display_section(title):
    """Print a nicely formatted section header to keep the output readable."""
    width = 60
    print("\n" + "=" * width)
    print(f"  {title}")
    print("=" * width)
