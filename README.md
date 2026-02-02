🎬 Movie Analytics Dashboard

An interactive movie analytics application built using Python, Pandas, and Streamlit.
This project enables users to explore and analyze movie data through filters, rankings, trends, and search functionality.

This project was developed as a college major project with a focus on:

Data analysis

Dashboard design

Python project structuring

Interactive visualizations

📌 Project Objective

The goal of this project is to analyze a movie dataset and present meaningful insights such as:

Rating trends over time

Top-rated genres and actors

High-performing movies

Filtered and search-based exploration

The project emphasizes analytical thinking and usability, not production deployment.

✨ Features
🔍 Search

Search movies by title or actor name

Displays top results sorted by rating

🎛️ Filters

Year range selection

Minimum rating filter

Minimum vote count filter

Genre filter

Language filter

📊 Dashboard Sections

Overview

Total movies

Average & median ratings

Year range

Production trend by year

Rating distribution

Top Genres

Highest-rated genres (with minimum movie threshold)

Top Actors

Highest-rated actors based on average rating

Top Movies

Top 50 movies by rating

Deep Dive

Genre-specific and actor-specific analysis

Data View

View filtered raw dataset

🧠 Technologies Used

Python

Pandas – data cleaning & analysis

Streamlit – interactive dashboard

Plotly – charts and visualizations

NumPy

📁 Project Structure
MOVIE/
│
├── app.py                     # Main Streamlit application
├── required.txt               # Project dependencies
├── final_movies.ipynb         # Data cleaning & preprocessing notebook
│
├── src/
│   ├── analytics.py           # MovieAnalyzer class (core analysis logic)
│   └── data_loader.py         # Dataset loading logic
│
├── data/
│   ├── movies.csv             # Original dataset
│   └── movies_cleaned.csv     # Cleaned dataset used in the app
│
├── .gitignore
└── .ipynb_checkpoints/

▶️ How to Run the Project Locally
1️⃣ Clone the repository
git clone https://github.com/your-username/movie-analytics-dashboard.git
cd MOVIE

2️⃣ Install dependencies
pip install -r required.txt

3️⃣ Run the Streamlit app
streamlit run app.py


The application will open in your browser at:

http://localhost:8501

📊 Dataset Information

The dataset contains movie metadata such as:

Title

Release year

Genres

Cast

Language

Ratings

Vote counts

movies.csv is the original dataset

movies_cleaned.csv is the cleaned and processed dataset used by the app

🎓 Academic Context

Developed as a college major project

Focus areas:

Data analysis using Pandas

Interactive dashboards with Streamlit

Filtering and aggregation logic

Clean and modular project structure

Deployment was not required for academic evaluation.



👤 Author

Dheeraj Rai
