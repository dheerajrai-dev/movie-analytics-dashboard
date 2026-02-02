import pandas as pd

class MovieAnalyzer:
    def __init__(self, df):
        self.df = df
        
        # 1. SPLIT GENRES (Now using comma since we fixed the CSV)
        if not self.df.empty and isinstance(self.df['genres'].iloc[0], str):
            self.df['genres_list'] = self.df['genres'].str.split(', ')

        # 2. SPLIT ACTORS
        if not self.df.empty and isinstance(self.df['cast'].iloc[0], str):
            self.df['cast_list'] = self.df['cast'].str.split(', ')

    # --- METRICS ---
    def get_kpis(self):
        return {
            "total_movies": len(self.df),
            "year_range": f"{self.df['year'].min()} - {self.df['year'].max()}",
            "avg_rating": self.df['vote_average'].mean(),
            "median_rating": self.df['vote_average'].median()
        }

    # --- TOP LISTS ---
    def get_top_genres(self, min_movies=30):
        # Explode: "Action, Adventure" becomes 2 rows (one for Action, one for Adventure)
        df_exploded = self.df.explode('genres_list')
        
        stats = df_exploded.groupby('genres_list').agg({
            'vote_average': 'mean',
            'title': 'count'
        }).rename(columns={'title': 'movie_count', 'vote_average': 'avg_rating'})
        
        return stats[stats['movie_count'] >= min_movies].sort_values(by='avg_rating', ascending=False)

    def get_top_actors(self, min_movies=10):
        df_exploded = self.df.explode('cast_list')
        stats = df_exploded.groupby('cast_list').agg({
            'vote_average': 'mean',
            'title': 'count'
        }).rename(columns={'title': 'movie_count', 'vote_average': 'avg_rating'})
        return stats[stats['movie_count'] >= min_movies].sort_values(by='avg_rating', ascending=False)

    # --- CHARTS ---
    def get_movies_per_year(self):
        return self.df.groupby('year').size().reset_index(name='count')

    # --- DEEP DIVE ---
    def get_movies_by_genre_specific(self, genre):
        # Finds movies where the genre list contains the specific genre
        mask = self.df['genres'].str.contains(genre, na=False)
        return self.df[mask].sort_values(by='vote_average', ascending=False)

    def get_movies_by_actor_specific(self, actor_name):
        mask = self.df['cast'].str.contains(actor_name, na=False)
        return self.df[mask].sort_values(by='vote_average', ascending=False)

    # --- SEARCH ---
    def search_movies(self, query):
        query = query.lower()
        mask_title = self.df['title'].str.lower().str.contains(query, na=False)
        mask_cast = self.df['cast'].str.lower().str.contains(query, na=False)
        return self.df[mask_title | mask_cast].sort_values(by='vote_average', ascending=False).head(20)