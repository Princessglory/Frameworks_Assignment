# ===============================
# Streamlit App
# ===============================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS

# -------------------------------
# Load the cleaned dataset
# -------------------------------
df = pd.read_csv("metadata_cleaned.csv")

# Make sure publish_year exists
if 'publish_year' not in df.columns:
    df['publish_year'] = pd.to_datetime(df['publish_time'], errors='coerce').dt.year

# -------------------------------
# App Title & Description
# -------------------------------
st.title("COVID-19 Research Papers Explorer")
st.write("Explore COVID-19 research papers interactively with simple visualizations.")

# -------------------------------
# Show a sample of the data
# -------------------------------
st.subheader("Sample of the Dataset")
st.dataframe(df.sample(5))  # Show 5 random rows

# -------------------------------
# Interactive Widget: Year Slider
# -------------------------------
year_min = int(df['publish_year'].min())
year_max = int(df['publish_year'].max())
selected_year = st.slider("Select Year", year_min, year_max, year_max)

# Filter data for selected year
df_year = df[df['publish_year'] == selected_year]
st.write(f"Number of papers in {selected_year}: {len(df_year)}")

# -------------------------------
# Visualization 1: Publications Over Time
# -------------------------------
st.subheader("Publications Over Time")
papers_per_year = df['publish_year'].value_counts().sort_index()
fig, ax = plt.subplots()
sns.lineplot(x=papers_per_year.index, y=papers_per_year.values, marker="o", ax=ax)
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
st.pyplot(fig)

# -------------------------------
# Visualization 2: Top 10 Journals
# -------------------------------
st.subheader("Top 10 Journals")
top_journals = df['journal'].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(x=top_journals.values, y=top_journals.index, palette="viridis", ax=ax)
ax.set_xlabel("Number of Papers")
ax.set_ylabel("Journal")
st.pyplot(fig)

# -------------------------------
# Visualization 3: Word Cloud of Titles
# -------------------------------
st.subheader("Word Cloud of Paper Titles")
title_text = " ".join(df['title'].astype(str))
wordcloud = WordCloud(width=800, height=400, stopwords=set(STOPWORDS),
                      background_color="white").generate(title_text)
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# -------------------------------
# Visualization 4: Papers by Source
# -------------------------------
st.subheader("Distribution by Source")
source_counts = df['source_x'].value_counts()
fig, ax = plt.subplots()
sns.barplot(x=source_counts.values, y=source_counts.index, palette="cubehelix", ax=ax)
ax.set_xlabel("Number of Papers")
ax.set_ylabel("Source")
st.pyplot(fig)
