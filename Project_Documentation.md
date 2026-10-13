# Project Documentation – Student Performance Analytics System

## 1. Project Title

**Student Performance Analytics System**

- **Student Name**: Medha
- **Course**: Python with AI – EWB Courses
- **Submission Date**: October 2026

---

## 2. Objective

The purpose of this project is to build a Python program that can read student academic data from a CSV file, process it, and produce a meaningful performance report. It answers questions like:

- What is the class average?
- Which students passed or failed?
- Which subject has the best performance?
- Who are the top students?

This kind of analysis is common in real-world educational settings, and building it helps in understanding how data processing works using Python libraries.

---

## 3. Technologies Used

| Tool / Library | Version Used | Why it was used                              |
|----------------|-------------|----------------------------------------------|
| Python         | 3.12        | Main programming language                    |
| Pandas         | 3.x         | To load CSV, create DataFrames, filter data  |
| NumPy          | 2.x         | For numerical operations on arrays           |

No web frameworks, databases, or ML libraries were used. The focus is entirely on Python fundamentals and data handling.

---

## 4. Dataset Description

The dataset is stored in `students.csv` and contains **20 records**. Each record represents one student with:

- A unique Student ID
- Their name and department
- Marks in 5 subjects: Math, Science, English, Computer, History (each out of 100)
- Attendance percentage

The data was manually created to have a good mix — some high scorers, some average, and a few who fall below the passing criteria.

---

## 5. Implementation

### 5.1 Loading the Data
Used `pd.read_csv("students.csv")` to load the file into a DataFrame. Printed the shape and checked for null values to make sure the data is clean before processing.

### 5.2 Calculating Totals and Averages
- **Total**: Sum of all 5 subject marks → `df[subjects].sum(axis=1)`
- **Average**: Mean of the 5 subjects → `df[subjects].mean(axis=1)`, rounded to 2 decimals

### 5.3 Assigning Grades
Wrote a function `assign_grade(avg)` that uses if-elif-else to return a letter grade:

```
90+   → A+
80-89 → A
70-79 → B
60-69 → C
50-59 → D
<50   → F
```

Applied it to the entire DataFrame using `.apply()`.

### 5.4 Pass/Fail Determination
A student passes only if **both** conditions are true:
1. Average marks ≥ 50
2. Attendance ≥ 60%

Used `numpy.where()` to create the Status column efficiently.

### 5.5 Class-Level Summary
Computed overall statistics using NumPy:
- `np.mean()`, `np.max()`, `np.min()`, `np.std()` on the Average column.
- Counted pass/fail using Pandas boolean filtering.

### 5.6 Subject-Wise Analysis
Looped through each subject column, converted marks to a NumPy array, and calculated mean/max/min. Stored results in a new DataFrame for clean display.

### 5.7 Department Grouping
Used `df.groupby("Department").agg(...)` to compute per-department statistics including average marks and pass rate.

### 5.8 Top Performers
Used `df.nlargest(5, "Average")` to get the top 5 students sorted by their average.

### 5.9 Grade Distribution
Used `value_counts()` on the Grade column and printed a simple text bar chart.

### 5.10 Attendance Analysis
Converted attendance to a NumPy array and computed summary stats. Flagged students with attendance below 65%.

---

## 6. Key Features

1. Modular code structure with separate `functions.py`
2. NumPy used for numerical computations throughout
3. Pandas used for data loading, filtering, grouping
4. Custom grading system with clear rules
5. Pass/fail logic combining marks and attendance
6. Subject-wise performance comparison
7. Department-wise summary with pass rates
8. Top 5 student identification
9. Grade distribution visualization (text-based)
10. Low attendance flagging

---

## 7. Output

The program prints a formatted report with sections for:
- Data overview
- Processed student table (with grades and status)
- Class summary statistics
- Subject performance table
- Top 5 students
- Department comparison
- Pass/fail breakdown
- Grade distribution chart
- Attendance overview

*(Screenshots can be added after running the program.)*

---

## 8. Final Outcome

The project works as intended. When `main.py` is run, it:
- Successfully loads all 20 records from the CSV
- Calculates derived columns (total, average, grade, status)
- Produces a complete analysis with multiple perspectives (per-student, per-subject, per-department)
- Displays everything in a clean, readable format

The program runs without errors and gives correct results for all calculations.

---

## 9. Challenges & Learnings

| Challenge | How I handled it |
|-----------|-----------------|
| Deciding the grading boundaries | Looked at common academic grading scales and picked one that gives a reasonable distribution with my dataset |
| Combining pass/fail conditions | Used `numpy.where()` with combined boolean conditions instead of writing a loop |
| Making output readable | Added section headers and formatted columns using `.to_string()` |
| Keeping code organized | Split functions into a separate file early on, which saved time during debugging |
| Edge cases in grading | Tested with students scoring exactly on the boundaries (e.g., 50, 60, 70) |

**What I learned:**
- How to structure a small Python project with multiple files
- Practical difference between NumPy array operations and Pandas methods
- How to use `.groupby()` and `.agg()` for grouped analysis
- Importance of checking data quality before processing

---

## 10. GitHub Repository

🔗 [Repository Link](#) *(will be updated after pushing to GitHub)*

---

*This documentation is submitted as part of the Python with AI mini project – EWB Courses, October 2026.*
