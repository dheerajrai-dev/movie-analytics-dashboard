# 🎬 Movie Analytics Dashboard

An interactive **movie analytics dashboard** built using **Python, Pandas, and Streamlit**.  
This application enables users to explore, filter, and analyze movie data through an intuitive and visually rich interface.

> 📌 **Academic Project**  
> Developed as a college major project with a focus on data analysis, visualization, and clean project structuring.

---

## 📊 Project Overview

The **Movie Analytics Dashboard** helps uncover meaningful insights from movie data, such as:

- 📈 Rating trends over time  
- 🎭 Top-rated genres and actors  
- ⭐ High-performing movies  
- 🔍 Search-based and filter-based exploration  

The goal of this project is to demonstrate **analytical thinking, dashboard design, and Python proficiency**, rather than production deployment.

---

## ✨ Key Features

### 🔍 Smart Search
- Search movies by **title** or **actor name**
- Results are sorted by rating for relevance

### 🎛️ Interactive Filters
- Year range slider  
- Minimum rating filter  
- Minimum vote count filter  
- Genre selection  
- Language selection  

### 📑 Dashboard Tabs
- **📊 Overview** – KPIs, trends, and rating distributions  
- **🎭 Top Genres** – Highest-rated genres (with thresholds)  
- **🌟 Top Actors** – Actors ranked by average ratings  
- **🎥 Top Movies** – Top 50 movies by rating  
- **📈 Deep Dive** – Genre- and actor-specific analysis  
- **📄 Data View** – Filtered raw dataset  

---

## 🧠 Tech Stack

- **Python**
- **Pandas** – Data analysis & manipulation  
- **Streamlit** – Interactive dashboard  
- **Plotly** – Data visualization  
- **NumPy**

---

## 📁 Project Structure

```text
movie-analytics-dashboard/
│
├── app.py                     # Main Streamlit application
├── required.txt               # Project dependencies
├── final_movies.ipynb         # Data cleaning & preprocessing notebook
│
├── src/
│   ├── analytics.py           # Core analytics logic
│   └── data_loader.py         # Dataset loading logic
│
├── data/
│   └── movies_cleaned.csv     # Cleaned dataset used in the app
│
└── README.md
```
▶️ How to Run the Project Locally

1️⃣ Install dependencies
pip install -r required.txt

2️⃣ Run the Streamlit app
streamlit run app.py

## 📊 Dataset Information

- Dataset Name: **Millions of Movies**
- Source: Kaggle  
- Link: https://www.kaggle.com/datasets/akshaypawar7/millions-of-movies

The dataset contains extensive movie metadata, including:
- Movie titles
- Release years
- Genres
- Cast information
- Languages
- Ratings and vote counts

> ⚠️ Note:  
> The original raw dataset is not included in this repository due to GitHub file size limitations.  
> A cleaned and processed version (`movies_cleaned.csv`) is used for analysis and is included in the project.


<h5>👤 Author
Dheeraj Rai </h5>
