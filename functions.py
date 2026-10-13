import numpy as np
import pandas as pd

SUBJECT_COLS = ["Math", "Science", "English", "Computer", "History"]


def load_data(filepath):
    df = pd.read_csv(filepath)
    print(f"Dataset loaded successfully - {len(df)} records found.\n")
    return df


def calculate_total(df):
    df["Total"] = df[SUBJECT_COLS].sum(axis=1)
    return df


def calculate_average(df):
    df["Average"] = df[SUBJECT_COLS].mean(axis=1).round(2)
    return df


def assign_grade(avg):
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
    df["Grade"] = df["Average"].apply(assign_grade)
    return df


def determine_pass_fail(df, passing_avg=50, min_attendance=60):
    conditions = (df["Average"] >= passing_avg) & (df["Attendance"] >= min_attendance)
    df["Status"] = np.where(conditions, "Pass", "Fail")
    return df


def get_class_summary(df):
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
    top = df.nlargest(n, "Average")[["Student_ID", "Name", "Department", "Average", "Grade"]]
    return top.reset_index(drop=True)


def department_summary(df):
    dept_stats = df.groupby("Department").agg(
        Students=("Student_ID", "count"),
        Dept_Average=("Average", "mean"),
        Pass_Count=("Status", lambda x: (x == "Pass").sum()),
    )
    dept_stats["Dept_Average"] = dept_stats["Dept_Average"].round(2)
    dept_stats["Pass_Rate(%)"] = ((dept_stats["Pass_Count"] / dept_stats["Students"]) * 100).round(1)
    return dept_stats


def display_section(title):
    width = 60
    print("\n" + "=" * width)
    print(f"  {title}")
    print("=" * width)
