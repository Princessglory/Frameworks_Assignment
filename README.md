# CORD-19 Data Analysis & Streamlit App

This repository contains a basic analysis of the [CORD-19 dataset](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) and a simple interactive Streamlit app to explore COVID-19 research papers.

---
## Project Overview

The project is divided into 4 parts:

1. **Data Loading and Exploration (Part 1)**
   - Load `metadata.csv` into a pandas DataFrame.
   - Explore data structure, dimensions, and missing values.

2. **Data Cleaning and Preparation (Part 2)**
   - Drop columns with >50% missing values.
   - Fill missing values in key text columns.
   - Create new columns like `publish_year` and `abstract_word_count`.
   - Save cleaned dataset as `metadata_cleaned.csv`.

3. **Data Analysis and Visualization (Part 3)**
   - Count papers by publication year.
   - Identify top journals publishing COVID-19 research.
   - Generate a word cloud from paper titles.
   - Plot distribution of paper counts by source.
   - Visualizations are created using **matplotlib**, **seaborn**, and **wordcloud**.

4. **Streamlit Application (Part 4)**
   - Interactive app (`app.py`) to explore the cleaned dataset.
   - Features:
     - Year range slider to filter publications.
     - Line chart of publications over time.
     - Bar chart of top 10 journals.
     - Word cloud of paper titles.
     - Bar chart of papers by source.
     - Display of a sample of the dataset.

---
## Screenshot

![Streamlit App Screenshot](/Streamlit%20App%20Screenshot.png) 

## Installation

1. Clone the repository:

```bash
git clone <https://github.com/Princessglory/Frameworks_Assignment.git>
cd Frameworks_Assignment

pip install pandas matplotlib seaborn streamlit wordcloud
```
2. Install required packages:
```
pip install pandas matplotlib seaborn streamlit wordcloud
```
Running the Streamlit App

Run the following command from the project folder:
```
python -m streamlit run app.py
```
* The app will open in your default web browser.

* Use the slider to filter by publication year and explore visualizations.


Project Files

* assignment.ipynb — Jupyter notebook with analysis and visualizations (Parts 1–3)

* app.py — Streamlit interactive application (Part 4)

* metadata.csv — Original dataset

* metadata_cleaned.csv — Cleaned dataset used in the notebook and app

* .gitignore — To ignore unnecessary files

## Author

Okogun Princess Glory