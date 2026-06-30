# 📊 Week 3: Data Handling & Python Libraries

Welcome to **Week 3** of the **AI Foundations to Generative AI** course.

This week focuses on one of the most important skills in AI and Data Science:

> **Working with data effectively.**

You will learn how to load, clean, analyze, and visualize data using Python's most popular data libraries.

---

## 🎯 Learning Outcomes

By the end of this week, you will be able to:

- Understand the role of data in AI systems
- Perform numerical computations using NumPy
- Analyze datasets using Pandas
- Clean messy real-world data
- Create visualizations using Matplotlib
- Identify trends, outliers, and correlations
- Explore modern tools such as Polars and Plotly

---

## 📂 Week Resources

| Resource | Description |
|-----------|-------------|
| Slide-notes | Detailed Study Notes |
| Exercise | NumPy, Pandas & Matplotlib Examples |
| Assignment | Dataset Analysis Mini Project |

---

## 📚 Topics Covered

### 1️⃣ NumPy – Fast Numerical Computing

Learn the foundation of scientific computing in Python.

Topics:

- NumPy Arrays
- Vectorized Operations
- Mathematical Functions
- Statistical Functions
- Matrix Operations

Example:

```python
import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr.mean())
print(arr.max())
```

---

### 2️⃣ Pandas – Data Analysis Made Easy

Learn how to work with tabular data like a professional data analyst.

Topics:

- Creating DataFrames
- Loading CSV Files
- Exploring Data
- Filtering Data
- Sorting Data
- Creating New Columns
- Data Cleaning
- GroupBy Operations

Example:

```python
import pandas as pd

df = pd.read_csv("students.csv")

print(df.head())
```

---

### 3️⃣ Data Cleaning

Real-world data is often incomplete and messy.

Topics:

- Missing Values
- Duplicate Records
- Data Type Conversion
- String Cleaning
- Data Validation

Example:

```python
df.dropna()

df.drop_duplicates()
```

---

### 4️⃣ Data Visualization with Matplotlib

Learn how to turn numbers into meaningful visual stories.

Topics:

- Bar Charts
- Line Charts
- Scatter Plots
- Histograms
- Pie Charts

Example:

```python
import matplotlib.pyplot as plt

plt.bar(
    ["A", "B", "C"],
    [80, 90, 75]
)

plt.show()
```

---

### 5️⃣ Understanding Data Patterns

Good analysts do more than calculate numbers.

They look for:

- 📈 Trends
- 🎯 Outliers
- 🔗 Correlations
- 🔄 Seasonality

Always ask:

> "What story is the data trying to tell?"

---

### 6️⃣ Modern Data Tools

#### Polars

A modern and faster alternative to Pandas.

Benefits:

- Faster performance
- Lower memory usage
- Better for large datasets

---

#### Plotly

Interactive data visualization library.

Features:

- Hover
- Zoom
- Filter
- Dashboard Integration

---

#### AI-Powered Data Analysis

Modern AI tools can assist with:

- Data Cleaning
- Data Exploration
- Code Generation
- Visualization Suggestions

Examples:

- ChatGPT
- Claude
- Gemini

---

## 📝 Assignment

### Assignment 03: Dataset Analysis Mini Project

Choose ONE level.

| Level | Activity |
|---------|----------|
| 🟢 Beginner | Titanic Dataset Analysis |
| 🔵 Intermediate | Custom Dataset Analysis |
| 🟠 Advanced | Personal Data Analysis |

➡️ Open: `Assignments/assignment-03-dataset-analysis.md`

---

## 🛠 Recommended Libraries

Install required libraries:

```bash
pip install numpy pandas matplotlib seaborn plotly
```

Import libraries:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

---

## 📌 Key Takeaways

- NumPy powers numerical computing.
- Pandas simplifies data analysis.
- Matplotlib helps visualize data.
- Data cleaning is a critical skill.
- Good analysts focus on insights, not just numbers.
- Modern tools make data analysis faster than ever.

---

## 🚀 What's Next?

### Week 4: Generative AI & NLP

Topics include:

- How ChatGPT Works
- Tokens and Embeddings
- Prompt Engineering
- Large Language Models (LLMs)
- Building AI Applications

Get ready to build your first AI-powered application.

---

## 💡 Quote of the Week

> "Data is the new oil, but insight is the real fuel."

Happy Learning! 🚀