# Student Performance Analytics System

A Python-based data analysis project that reads student records from a CSV file, processes the data using **NumPy** and **Pandas**, and generates a detailed performance report.

---

## Project Overview

| Detail           | Info                                      |
|------------------|-------------------------------------------|
| **Author**       | Aditya Medhane                            |
| **Course**       | Python with AI – EWB Courses              |
| **Date**         | October 2026                              |
| **Language**     | Python 3.x                                |
| **Libraries**    | Pandas, NumPy                             |

## Objective

The goal of this project is to build a simple yet functional analytics system that can:

- Load student data (marks, attendance, department info) from a CSV file.
- Compute totals, averages, and letter grades for each student.
- Determine pass/fail status based on marks and attendance criteria.
- Perform subject-wise and department-wise analysis.
- Identify top-performing students and present a clear summary report.

This project demonstrates practical usage of Python fundamentals — functions, loops, conditionals — along with NumPy for numerical computation and Pandas for data manipulation.

---

## Technologies Used

| Technology | Purpose                                         |
|------------|--------------------------------------------------|
| Python 3   | Core programming language                        |
| Pandas     | Reading CSV, DataFrame operations, filtering     |
| NumPy      | Numerical calculations (mean, std, max, min)     |

No external APIs, databases, or machine learning libraries were used. The project is purely a data-analysis exercise using the concepts covered in class.

---

## Dataset Description

The dataset (`students.csv`) contains **20 student records** with the following columns:

| Column       | Description                           |
|--------------|---------------------------------------|
| Student_ID   | Unique identifier for each student    |
| Name         | Full name of the student              |
| Department   | Department code (CSE, ECE, ME, EE)    |
| Math         | Marks in Mathematics (out of 100)     |
| Science      | Marks in Science (out of 100)         |
| English      | Marks in English (out of 100)         |
| Computer     | Marks in Computer Science (out of 100)|
| History      | Marks in History (out of 100)         |
| Attendance   | Attendance percentage                 |

The data includes a realistic spread of marks — some students score very well, some are average, and a few fall below the passing criteria.

---

## Project Structure

```
student-performance-analytics/
│
├── main.py            # Entry point – runs the full analysis
├── functions.py       # All reusable helper functions
├── students.csv       # Student dataset (20 records)
├── README.md          # Project documentation (this file)
└── Project_Documentation.md   # Detailed project report
```

---

## Implementation Details

### Step 1 – Preparing the Dataset
Created a CSV file with 20 student records covering 4 departments and 5 subjects, with varied marks and attendance values to make the analysis meaningful.

### Step 2 – Loading the Data
Used `pandas.read_csv()` to load the dataset into a DataFrame. Printed basic info like shape, column names, and checked for missing values.

### Step 3 – Processing the Data
- **Total marks**: Summed across all five subjects using `df[columns].sum(axis=1)`.
- **Average marks**: Calculated using `df[columns].mean(axis=1)`, rounded to 2 decimal places.
- **Grades**: Assigned using a custom function with if-elif conditions:
  - A+ (≥90), A (≥80), B (≥70), C (≥60), D (≥50), F (<50)
- **Pass/Fail**: A student passes if their average is ≥ 50 **and** attendance is ≥ 60%. Used `numpy.where()` for this.

### Step 4 – Analysis
- **Class summary**: Overall average, highest/lowest marks, standard deviation, pass/fail counts.
- **Subject-wise analysis**: Mean, max, and min marks per subject — helps identify strong and weak subjects.
- **Top 5 students**: Sorted by average marks in descending order.
- **Department comparison**: Average marks and pass rate grouped by department.
- **Grade distribution**: Count of students in each grade category.
- **Attendance overview**: Average, max, min attendance and flagging students below 65%.

### Step 5 – Displaying Results
All output is printed in clearly formatted sections with headers, making it easy to read directly from the console.

---

## Key Features

1. **Modular code** – Functions are separated into `functions.py` for reusability.
2. **NumPy usage** – Used for computing mean, standard deviation, max/min on arrays.
3. **Pandas usage** – DataFrame operations for filtering, grouping, and aggregation.
4. **Grade assignment** – Custom grading function applied to every student.
5. **Pass/Fail logic** – Based on both marks and attendance thresholds.
6. **Subject-wise stats** – Identifies the best and weakest subjects across the class.
7. **Department comparison** – Groups data by department for comparative analysis.
8. **Top performers** – Lists the top 5 students by average marks.
9. **Grade distribution** – Simple text-based bar chart in the console.
10. **Attendance flagging** – Highlights students with low attendance.

---

## How to Run

1. Make sure Python 3 is installed on your system.
2. Install the required libraries (if not already available):
   ```
   pip install pandas numpy
   ```
3. Clone or download this repository.
4. Open a terminal in the project folder and run:
   ```
   python main.py
   ```

---

## Sample Output

When you run `main.py`, you will see sections like:

```
============================================================
  LOADING DATASET
============================================================
Dataset loaded successfully — 20 records found.

============================================================
  CLASS SUMMARY
============================================================
  Class Average        : 68.43
  Highest Average      : 91.4
  ...

============================================================
  TOP 5 STUDENTS
============================================================
 Student_ID         Name Department  Average Grade
        104   Sneha Patel        CSE    91.40    A+
        ...
```

*(Actual values will be computed from the dataset when you run the program.)*

---

## Final Outcome

The project successfully:
- Loads and validates the student dataset.
- Computes per-student metrics (total, average, grade, pass/fail).
- Performs class-level, subject-level, and department-level analysis.
- Presents everything in a clean, readable console output.

It covers all the core Python concepts taught in the course — functions, loops, conditionals, NumPy operations, and Pandas DataFrame usage.

---

## Challenges & Learnings

- **Structuring the code**: Initially had everything in a single file. Splitting into `main.py` and `functions.py` made the code much cleaner and easier to debug.
- **Grading logic**: Had to decide on a fair grading scale and test it with edge cases (e.g., a student scoring exactly 50).
- **Pass/fail criteria**: Combining two conditions (marks + attendance) required careful use of logical operators.
- **Formatting output**: Spent time making the console output readable with section headers and aligned columns.
- **NumPy vs Pandas**: Learnt when to use NumPy arrays directly vs. Pandas built-in methods — both have their place.

---

## Live Demo

🌐 [https://student-performance-analytics-khaf7czsjvwblmv3qwnbao.streamlit.app](https://student-performance-analytics-khaf7czsjvwblmv3qwnbao.streamlit.app/)

## GitHub Repository

🔗 [https://github.com/M23adi/student-performance-analytics](https://github.com/M23adi/student-performance-analytics)

---

*Submitted as part of the Python with AI mini project – EWB Courses, October 2026.*
