import pandas as pd
import numpy as np

from functions import (
    load_data,
    calculate_total,
    calculate_average,
    assign_grades,
    determine_pass_fail,
    get_class_summary,
    subject_wise_analysis,
    top_performers,
    department_summary,
    display_section,
    SUBJECT_COLS,
)


def main():

    display_section("LOADING DATASET")
    df = load_data("students.csv")

    print("First 5 records:")
    print(df.head().to_string(index=False))
    print(f"\nColumns : {list(df.columns)}")
    print(f"Shape   : {df.shape[0]} rows x {df.shape[1]} columns")

    display_section("DATA OVERVIEW")
    print(df.describe().round(2).to_string())

    missing = df.isnull().sum().sum()
    if missing == 0:
        print("\nNo missing values found - data is clean.")
    else:
        print(f"\nWarning: {missing} missing value(s) detected.")

    display_section("PROCESSING DATA")

    df = calculate_total(df)
    df = calculate_average(df)
    df = assign_grades(df)
    df = determine_pass_fail(df)

    print("Added columns: Total, Average, Grade, Status")
    print("\nProcessed data (showing key columns):\n")
    cols_to_show = ["Student_ID", "Name", "Department", "Total", "Average", "Grade", "Status"]
    print(df[cols_to_show].to_string(index=False))

    display_section("CLASS SUMMARY")

    summary = get_class_summary(df)
    for key, val in summary.items():
        print(f"  {key:20s} : {val}")

    pass_pct = round((summary["Passed"] / summary["Total Students"]) * 100, 1)
    print(f"\n  Overall pass rate   : {pass_pct}%")

    display_section("SUBJECT-WISE PERFORMANCE")

    subj_df = subject_wise_analysis(df)
    print(subj_df.to_string(index=False))

    best_subj = subj_df.loc[subj_df["Average"].idxmax(), "Subject"]
    weak_subj = subj_df.loc[subj_df["Average"].idxmin(), "Subject"]
    print(f"\nBest performing subject  : {best_subj}")
    print(f"Needs improvement       : {weak_subj}")

    display_section("TOP 5 STUDENTS")

    top = top_performers(df, n=5)
    print(top.to_string(index=False))

    topper = df.loc[df["Average"].idxmax()]
    print(f"\nOverall topper: {topper['Name']} ({topper['Department']}) "
          f"with an average of {topper['Average']}")

    display_section("DEPARTMENT-WISE COMPARISON")

    dept_df = department_summary(df)
    print(dept_df.to_string())

    display_section("PASS / FAIL DETAILS")

    passed_students = df[df["Status"] == "Pass"]
    failed_students = df[df["Status"] == "Fail"]

    print(f"Passed : {len(passed_students)}")
    print(f"Failed : {len(failed_students)}\n")

    if len(failed_students) > 0:
        print("Students who failed:")
        print(failed_students[["Student_ID", "Name", "Average", "Attendance", "Status"]].to_string(index=False))

    display_section("GRADE DISTRIBUTION")

    grade_counts = df["Grade"].value_counts().sort_index()
    for grade, count in grade_counts.items():
        bar = "#" * count
        print(f"  {grade:3s} : {bar} ({count})")

    display_section("ATTENDANCE OVERVIEW")

    att = np.array(df["Attendance"])
    print(f"  Average attendance  : {np.mean(att):.1f}%")
    print(f"  Highest attendance  : {np.max(att)}%")
    print(f"  Lowest attendance   : {np.min(att)}%")

    low_att = df[df["Attendance"] < 65]
    if len(low_att) > 0:
        print(f"\n  Students with attendance below 65%:")
        print(low_att[["Student_ID", "Name", "Attendance"]].to_string(index=False))

    display_section("ANALYSIS COMPLETE")
    print("All results have been generated successfully.")
    print("Thank you for using the Student Performance Analytics System!\n")


if __name__ == "__main__":
    main()
