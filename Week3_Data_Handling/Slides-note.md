# 📘 Week 3: Data Handling & Python Libraries

## 🎯 Learning Objectives

By the end of this week, students will be able to:

- Understand why data is important in AI
- Use NumPy for numerical computing
- Use Pandas for data analysis and manipulation
- Clean and prepare real-world datasets
- Create visualizations using Matplotlib
- Identify trends, outliers, and patterns in data
- Explore modern data tools such as Polars and Plotly

---

# Part 1: NumPy

## What is NumPy?

NumPy (Numerical Python) is the foundation of scientific computing in Python.

### Why NumPy?

- Faster than Python lists
- Supports vectorized operations
- Used by TensorFlow, PyTorch, OpenCV, Scikit-Learn
- Handles large numerical datasets efficiently

### Example

```python
import numpy as np

prices = np.array([100, 150, 200, 250, 300])

discounted = prices * 0.9

print(discounted)
print(prices.mean())
print(prices.max())
print(prices.std())
```

### Key Concepts

- Arrays
- Vectorization
- Statistics
- Matrix Operations
- Broadcasting

---

# Part 2: Pandas

## What is Pandas?

Pandas is the most popular Python library for working with tabular data.

Think of Pandas as:

> Excel for Programmers

### What Can Pandas Do?

- Load CSV files
- Clean messy data
- Filter records
- Group and summarize data
- Perform data analysis

### Import Pandas

```python
import pandas as pd
```

---

# Creating a DataFrame

```python
import pandas as pd

data = {
    "name": ["Aisha", "Bibek", "Sita", "Roshan"],
    "age": [21, 20, 22, 21],
    "marks": [78, 82, 91, 65]
}

df = pd.DataFrame(data)

df
```

---

# Exploring Data

```python
df.head()

df.shape

df.info()

df.describe()
```

### Useful Functions

| Function | Purpose |
|-----------|-----------|
| head() | First rows |
| tail() | Last rows |
| shape | Rows and columns |
| info() | Data types |
| describe() | Statistics |

---

# Filtering Data

## Students Older Than 20

```python
df[df["age"] > 20]
```

## Multiple Conditions

```python
df[
    (df["age"] > 20)
    &
    (df["marks"] > 80)
]
```

## Select Columns

```python
df[["name", "marks"]]
```

---

# Sorting Data

```python
df.sort_values(
    "marks",
    ascending=False
)
```

---

# Creating New Columns

```python
df["passed"] = df["marks"] >= 50
```

```python
df["bonus"] = 5

df["final_marks"] = df["marks"] + df["bonus"]
```

---

# Cleaning Messy Data

## Missing Values

```python
df.isnull().sum()
```

```python
df.dropna()
```

```python
df.fillna(0)
```

---

## Duplicate Records

```python
df.drop_duplicates()
```

---

## Changing Data Types

```python
df["age"] = df["age"].astype(int)
```

---

# GroupBy: The Killer Feature

## Average Marks By Class

```python
df.groupby("class")["marks"].mean()
```

## Multiple Statistics

```python
df.groupby("class")["marks"].agg(
    ["mean", "max", "min", "count"]
)
```

### Why GroupBy Matters

GroupBy allows us to:

- Summarize data
- Compare categories
- Generate reports
- Discover insights quickly

---

# Part 3: Data Visualization

## What is Matplotlib?

Matplotlib helps us turn data into charts.

> A chart communicates 1000 numbers in 1 image.

---

# Import Matplotlib

```python
import matplotlib.pyplot as plt
```

---

# Bar Chart

```python
plt.bar(
    df["name"],
    df["marks"]
)

plt.title("Student Marks")

plt.show()
```

### Use Case

Compare categories.

Examples:

- Student marks
- Sales by region
- Revenue by product

---

# Line Chart

```python
months = ["Jan", "Feb", "Mar", "Apr"]

sales = [100, 120, 150, 180]

plt.plot(months, sales)

plt.show()
```

### Use Case

Show trends over time.

---

# Scatter Plot

```python
plt.scatter(
    df["age"],
    df["marks"]
)

plt.show()
```

### Use Case

Find relationships between variables.

---

# Histogram

```python
plt.hist(df["marks"])

plt.show()
```

### Use Case

Understand distributions.

---

# Pie Chart

```python
df["class"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.show()
```

### Use Case

Show proportions and percentages.

---

# Choosing the Right Chart

| Chart | Best For |
|---------|----------|
| Bar | Comparing categories |
| Line | Trends over time |
| Scatter | Relationships |
| Histogram | Distribution |
| Pie | Percentages |

---

# Spotting Patterns in Data

Good analysts look for:

## Trends

Values increasing or decreasing over time.

## Outliers

Unusual values that stand out.

## Correlations

Two variables moving together.

## Seasonality

Patterns that repeat over time.

### Always Ask

> What's unusual here?

---

# Modern Data Tools

## Polars

A modern DataFrame library.

### Benefits

- Built in Rust
- Faster than Pandas
- Great for large datasets

### Learning Path

```text
Python
↓
NumPy
↓
Pandas
↓
Matplotlib
↓
Polars
```

---

## Plotly

Interactive visualization library.

### Features

- Hover
- Zoom
- Filter
- Dashboard Integration

### Common Stack

```text
Python
↓
Pandas
↓
Plotly
↓
Streamlit
```

---

# AI-Powered Data Cleaning

Modern AI tools can help with:

- Finding duplicates
- Fixing formatting
- Cleaning text
- Generating analysis code

Examples:

- ChatGPT
- Claude
- Gemini

---

# Public Datasets

Useful Dataset Sources:

- Kaggle
- Hugging Face Datasets
- Google Dataset Search

Topics:

- Finance
- Health
- Sports
- Climate
- Sentiment Analysis
- Images and Audio

---

# Critical Thinking

## Important Reminder

> A chart that looks neutral can still mislead.

Common tricks:

- Truncated Y-Axis
- Cherry-Picked Time Ranges
- Misleading Colors

Always question the chart before trusting it.

---

# Assignment

## Mini Project: Dataset Analysis

Choose one level.

### 🟢 Beginner

Analyze Titanic Dataset

Requirements:

- 3 charts
- 3 insights

---

### 🔵 Intermediate

Choose any Kaggle dataset

Requirements:

- Data Cleaning
- Data Analysis
- 3 Charts
- 3 Insights

---

### 🟠 Advanced

Analyze Personal Data

Examples:

- Expenses
- Fitness Data
- Screen Time
- NEPSE Portfolio

Requirements:

- Notebook
- Visualizations
- 1 Page Report

---

# Key Takeaways

✅ NumPy powers numerical computing

✅ Pandas simplifies data analysis

✅ Matplotlib visualizes data

✅ Cleaning data is a critical skill

✅ Data tells stories through patterns

✅ Visualization helps communicate insights

---

# Next Week

## Week 4: Generative AI & NLP

Topics:

- How ChatGPT Works
- Tokens
- Embeddings
- Prompt Engineering
- Building AI Applications

🚀 See you in Week 4!