import streamlit as st
import pandas as pd
import plotly.express as px
from src.data_loader import load_data
from src.analytics import MovieAnalyzer

st.set_page_config(page_title="Movie Analytics Pro", layout="wide", page_icon="🎬")

# Load Data
df = load_data()
if df.empty:
    st.error("❌ Data not found! Run 'clean_final.py' first.")
    st.stop()

# --- HEADER & SEARCH ---
header_col1, header_col2 = st.columns([3, 1])
with header_col1:
    st.title("🎬 Movie Analytics Dashboard")
with header_col2:
    st.write("##")
    search_query = st.text_input("🔍 Search", placeholder="Title or Actor...", label_visibility="collapsed")

analyzer = MovieAnalyzer(df)

# --- SEARCH RESULTS ---
if search_query:
    st.divider()
    st.subheader(f"Search Results for '{search_query}'")
    results = analyzer.search_movies(search_query)
    if not results.empty:
        for _, row in results.iterrows():
            with st.container():
                c1, c2 = st.columns([1, 4])
                with c1:
                    st.metric("Rating", f"{row['vote_average']} ⭐", f"{int(row['vote_count'])} votes")
                with c2:
                    st.subheader(f"{row['title']} ({row['year']})")
                    st.caption(f"**Genres:** {row['genres']}")
                    st.write(row['overview'])
                st.divider()
    else:
        st.warning("No movies found.")
    st.stop()

# --- SIDEBAR ---
st.sidebar.header("🎛️ Dashboard Controls")

with st.sidebar.expander("🛠️ Total Movies"):
    st.write(f"**Total Movies:** {len(df):,}")

# A. Time
min_year, max_year = int(df['year'].min()), int(df['year'].max())
selected_years = st.sidebar.slider("📅 Year Range", min_year, max_year, (min_year, max_year))

# B. Filters
min_rating = st.sidebar.slider("⭐ Min Rating", 0.0, 10.0, 0.0, step=0.1)
min_votes = st.sidebar.slider("⚖️ Min Votes", 0, 5000, 0, step=50)

# C. Genre (NOW CLEAN!)
# We split by comma to get individual genres for the dropdown
all_genres = sorted(set([g for sublist in df['genres'].str.split(', ') for g in sublist]))
selected_genre = st.sidebar.selectbox("🎭 Genre", ["All Genres"] + all_genres)



# E. Language
languages = sorted(df['language'].unique().tolist())
if 'English' in languages: languages.insert(0, languages.pop(languages.index('English')))
selected_language = st.sidebar.selectbox("🌍 Language", ["All Languages"] + languages)

# --- FILTERING ---
filtered_df = df.copy()


filtered_df = filtered_df[(filtered_df['year'] >= selected_years[0]) & (filtered_df['year'] <= selected_years[1])]
filtered_df = filtered_df[filtered_df['vote_average'] >= min_rating]
filtered_df = filtered_df[filtered_df['vote_count'] >= min_votes]

if selected_genre != "All Genres":
    filtered_df = filtered_df[filtered_df['genres'].str.contains(selected_genre, na=False)]

if selected_language != "All Languages":
    filtered_df = filtered_df[filtered_df['language'] == selected_language]

filtered_analyzer = MovieAnalyzer(filtered_df)

# --- TABS ---
tabs = st.tabs(["📊 Overview", "🎭 Top Genres", "🌟 Top Actors", "🎥 Top Movies", "📈 Deep Dive", "📄 Data"])

# TAB 1: OVERVIEW
with tabs[0]:
    if not filtered_df.empty:
        kpis = filtered_analyzer.get_kpis()
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Movies", f"{kpis['total_movies']:,}")
        c2.metric("Avg Rating", f"{kpis['avg_rating']:.2f} ⭐")
        c3.metric("Median Rating", f"{kpis['median_rating']:.2f} ⭐")
        c4.metric("Year Range", kpis['year_range'])
        st.divider()
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("Production Trend")
            st.plotly_chart(px.line(filtered_analyzer.get_movies_per_year(), x='year', y='count', markers=True), use_container_width=True)
        with c2:
            st.subheader("Rating Distribution")
            st.plotly_chart(px.histogram(filtered_df, x="vote_average", nbins=20, color_discrete_sequence=['#636EFA']), use_container_width=True)

# TAB 2: TOP GENRES
with tabs[1]:
    st.subheader("Top Rated Genres")
    top_genres = filtered_analyzer.get_top_genres(min_movies=20)
    if not top_genres.empty:
        c1, c2 = st.columns([2, 1])
        with c1:
            st.plotly_chart(px.bar(top_genres.head(10), x=top_genres.head(10).index, y='avg_rating', color='avg_rating', title="Top 10 Genres", color_continuous_scale='Viridis'), use_container_width=True)
        with c2:
            st.dataframe(top_genres.head(10))

# TAB 3: TOP ACTORS
with tabs[2]:
    st.subheader("Top Rated Actors")
    top_actors = filtered_analyzer.get_top_actors(min_movies=5)
    if not top_actors.empty:
        c1, c2 = st.columns([2, 1])
        with c1:
            fig = px.bar(top_actors.head(10), x='avg_rating', y=top_actors.head(10).index, orientation='h', color='avg_rating', title="Top 10 Actors")
            fig.update_layout(yaxis=dict(autorange="reversed"))
            st.plotly_chart(fig, use_container_width=True)
        with c2:
            st.dataframe(top_actors.head(10))

# TAB 4: TOP MOVIES
with tabs[3]:
    st.subheader("Top 50 Movies")
    st.dataframe(filtered_df.sort_values(by='vote_average', ascending=False).head(50)[['title', 'year', 'vote_average', 'vote_count', 'genres', 'main_actors']], hide_index=True)

# TAB 5: DEEP DIVE
with tabs[4]:
    c1, c2 = st.columns(2)
    with c1:
        dive_genre = st.selectbox("Pick Genre", all_genres)
        gm = filtered_analyzer.get_movies_by_genre_specific(dive_genre)
        if not gm.empty:
            st.metric(f"Avg Rating ({dive_genre})", f"{gm['vote_average'].mean():.2f}")
            st.dataframe(gm[['title', 'vote_average']].head(10), hide_index=True)
    with c2:
        acts = filtered_analyzer.get_top_actors(min_movies=5).index.tolist()
        if acts:
            dive_actor = st.selectbox("Pick Actor", acts[:100])
            am = filtered_analyzer.get_movies_by_actor_specific(dive_actor)
            st.metric(f"Avg Rating ({dive_actor})", f"{am['vote_average'].mean():.2f}")
            st.dataframe(am[['title', 'year', 'vote_average']].head(10), hide_index=True)

# TAB 6: DATA
with tabs[5]:
    st.dataframe(filtered_df)