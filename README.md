# 📊 Student Performance Analysis using NumPy

**Author:** Shaurya

---

## 🧠 Overview

This project demonstrates how to analyze student performance data using **NumPy** in Python. It covers operations like totals, averages, ranking, filtering, grading, and basic data insights.

---

## 📁 Dataset

* **Students:** Shaurya, Pranav, Soham
* **Subjects:** Science, Maths
* **Marks Matrix:**

| Student | Science | Maths |
| ------- | ------- | ----- |
| Shaurya | 99      | 95    |
| Pranav  | 85      | 67    |
| Soham   | 89      | 50    |

---

## ⚙️ Features Implemented

### ✅ 1. Display Student Marks

Prints each student with their respective subject marks.

### 📐 2. Array Shape

Displays the dimensions of the marks matrix (Rows × Columns).

### ➕ 3. Total Marks

* Per student
* Per subject

### 📊 4. Average Calculation

* Subject-wise average
* Student-wise average

### 🏆 5. Topper Identification

Finds the student with the highest total marks.

### 📚 6. Subject Analysis

* Strongest subject (highest average)
* Weakest subject (lowest average)

### ✔️ 7. Pass/Fail Result

* Pass: Marks ≥ 40
* Fail: Marks < 40

### 🎓 8. Grading System

| Marks Range | Grade |
| ----------- | ----- |
| 90–100      | A+    |
| 80–89       | A     |
| 70–79       | B1    |
| 60–69       | B2    |
| 50–59       | C+    |
| 40–49       | C     |
| <40         | F     |

---

### 🔍 9. Filtered Data

* Students scoring **less than 70 average**
* Students scoring **more than 80 in any subject**

---

### 🔄 10. Broadcasting

Adds **+5 grace marks** to all students using NumPy broadcasting.

---

### 📈 11. Final Summary

* Overall average marks
* Highest marks
* Lowest marks

---

## 🛠️ Technologies Used

* Python 🐍
* NumPy 📦

---

## ▶️ How to Run

1. Install NumPy:

   ```bash
   pip install numpy
   ```

2. Run the script:

   ```bash
   python main.py
   ```

---

## 📌 Example Output Highlights

* Topper: Shaurya
* Strongest Subject: Science
* Weakest Subject: Maths
* Overall Average: Calculated dynamically

---

## 💡 Learning Outcomes

* Working with NumPy arrays
* Applying statistical functions
* Using indexing, filtering, and broadcasting
* Writing clean and structured analysis code

---

## 🚀 Future Improvements

* Add visualization using Matplotlib / Seaborn
* Accept dynamic user input
* Export results to CSV/Excel
* Build a simple dashboard

---

## 📜 License

This project is open-source and free to use.

---

✨ *Simple, clean, and powerful data analysis with NumPy!*
