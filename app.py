from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

DATA_PATH = Path(__file__).resolve().parent / "Week-04-Vibe-Coding-101" / "data" / "movie_ratings.csv"

st.title("MovieLens dashboard")
st.write("Using `Week-04-Vibe-Coding-101/data/movie_ratings.csv`.")

ratings = pd.read_csv(DATA_PATH)

st.header("Question 1 — Genre breakdown")
st.write(
    "What's the distribution of genres among the **movies that were rated**?"
)

st.subheader("How multi-genre movies are counted")
st.write(
    "The `genres` column is pipe-separated, e.g. `Crime|Drama`. "
    "Before counting, each movie is split on `|` so it appears once in **each** of its genres. "
    "We then count **distinct movies** per genre (not ratings). "
    "So *Jackie Brown* (`Crime|Drama`) adds 1 to Crime and 1 to Drama, not a combined 'Crime|Drama' slice. "
    "A pie chart would be a bad fit here (about 18 genres), so this is a **sorted horizontal bar chart**."
)

movies = ratings.drop_duplicates(subset=["movie_id"]).copy()
movies["genre"] = movies["genres"].str.split("|")
by_genre = (
    movies.explode("genre")
    .assign(genre=lambda d: d["genre"].str.strip())
    .groupby("genre", as_index=False)
    .agg(n_movies=("movie_id", "nunique"))
    .sort_values("n_movies", ascending=True)
)

fig = px.bar(
    by_genre,
    x="n_movies",
    y="genre",
    orientation="h",
    title="Rated movies per genre (sorted)",
    labels={"n_movies": "Number of movies", "genre": "Genre"},
)
st.plotly_chart(fig, use_container_width=True)
st.dataframe(by_genre.sort_values("n_movies", ascending=False), hide_index=True)

st.header("Question 2 — Genre satisfaction")
st.write("Which genres have the highest average rating? Which have the lowest?")
st.write(
    "Same `|` split as Question 1. Average = mean of **all ratings** tagged with that genre "
    "(a `Crime|Drama` rating is included in both Crime and Drama). "
    "Vertical bar chart, sorted by average (not alphabetical)."
)

genre_ratings = ratings.copy()
genre_ratings["genre"] = genre_ratings["genres"].str.split("|")
genre_ratings = genre_ratings.explode("genre")
genre_ratings["genre"] = genre_ratings["genre"].str.strip()

genre_avg = (
    genre_ratings.groupby("genre", as_index=False)
    .agg(avg_rating=("rating", "mean"), n_ratings=("rating", "size"))
    .sort_values("avg_rating", ascending=False)
)

fig_avg = px.bar(
    genre_avg,
    x="genre",
    y="avg_rating",
    category_orders={"genre": genre_avg["genre"].tolist()},
    hover_data={"n_ratings": True, "avg_rating": ":.2f"},
    title="Average rating by genre (sorted)",
    labels={"avg_rating": "Average rating", "genre": "Genre"},
)
fig_avg.update_xaxes(tickangle=-40)
fig_avg.update_yaxes(range=[0, 5])
st.plotly_chart(fig_avg, use_container_width=True)

highest = genre_avg.iloc[0]
lowest = genre_avg.iloc[-1]
col_hi, col_lo = st.columns(2)
col_hi.metric("Highest average", f"{highest['genre']}", f"{highest['avg_rating']:.2f}")
col_lo.metric("Lowest average", f"{lowest['genre']}", f"{lowest['avg_rating']:.2f}")
st.dataframe(
    genre_avg.sort_values("avg_rating", ascending=False),
    hide_index=True,
)

st.header("Question 3 — Ratings over time")
st.write("How has the mean rating changed across **movie release years**?")
st.write(
    "This uses the `year` column (when the movie came out), **not** `rating_year` "
    "(when the user submitted the rating). Mean = average of all ratings for movies released that year. "
    "Line chart because this is a trend over time. Rows with a missing release year are dropped."
)

by_year = (
    ratings.dropna(subset=["year"])
    .assign(release_year=lambda d: d["year"].astype(int))
    .groupby("release_year", as_index=False)
    .agg(mean_rating=("rating", "mean"), n_ratings=("rating", "size"))
    .sort_values("release_year")
)

fig_year = px.line(
    by_year,
    x="release_year",
    y="mean_rating",
    markers=True,
    hover_data={"n_ratings": True, "mean_rating": ":.2f"},
    title="Mean rating by movie release year",
    labels={"release_year": "Release year", "mean_rating": "Mean rating"},
)
fig_year.update_yaxes(range=[0, 5])
st.plotly_chart(fig_year, use_container_width=True)

st.header("Question 4 — Best movies, with a floor")
st.write(
    "What are the top 5 best-rated movies if we only count movies with at least **50** ratings? "
    "What changes if we raise that floor to **150**?"
)
st.write(
    "Floor = minimum number of ratings a movie must have. Without a floor, a movie with one 5-star "
    "could beat a famous movie with hundreds of ratings. Rank is by average rating, then by how many ratings."
)

movie_stats = (
    ratings.groupby(["movie_id", "title"], as_index=False)
    .agg(avg_rating=("rating", "mean"), n_ratings=("rating", "size"))
)


def top5_with_floor(stats, floor: int) -> pd.DataFrame:
    eligible = stats[stats["n_ratings"] >= floor]
    return eligible.sort_values(
        ["avg_rating", "n_ratings"], ascending=[False, False]
    ).head(5)


top50 = top5_with_floor(movie_stats, 50)
top150 = top5_with_floor(movie_stats, 150)

col50, col150 = st.columns(2)
with col50:
    st.subheader("Floor = 50")
    fig50 = px.bar(
        top50.sort_values("avg_rating", ascending=True),
        x="avg_rating",
        y="title",
        orientation="h",
        hover_data={"n_ratings": True, "avg_rating": ":.2f"},
        title="Top 5 (≥ 50 ratings)",
        labels={"avg_rating": "Average rating", "title": "Movie"},
    )
    fig50.update_xaxes(range=[0, 5])
    st.plotly_chart(fig50, use_container_width=True)
    st.dataframe(top50[["title", "avg_rating", "n_ratings"]], hide_index=True)

with col150:
    st.subheader("Floor = 150")
    fig150 = px.bar(
        top150.sort_values("avg_rating", ascending=True),
        x="avg_rating",
        y="title",
        orientation="h",
        hover_data={"n_ratings": True, "avg_rating": ":.2f"},
        title="Top 5 (≥ 150 ratings)",
        labels={"avg_rating": "Average rating", "title": "Movie"},
    )
    fig150.update_xaxes(range=[0, 5])
    st.plotly_chart(fig150, use_container_width=True)
    st.dataframe(top150[["title", "avg_rating", "n_ratings"]], hide_index=True)

st.subheader("Try another floor")
floor = st.slider("Minimum number of ratings", min_value=1, max_value=300, value=50, step=1)
custom = top5_with_floor(movie_stats, floor)
if custom.empty:
    st.warning("No movies meet this floor.")
else:
    fig_custom = px.bar(
        custom.sort_values("avg_rating", ascending=True),
        x="avg_rating",
        y="title",
        orientation="h",
        hover_data={"n_ratings": True, "avg_rating": ":.2f"},
        title=f"Top 5 (≥ {floor} ratings)",
        labels={"avg_rating": "Average rating", "title": "Movie"},
    )
    fig_custom.update_xaxes(range=[0, 5])
    st.plotly_chart(fig_custom, use_container_width=True)
