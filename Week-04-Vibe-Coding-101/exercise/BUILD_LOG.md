# Week 4 Vibe Coding — build log (raw notes)

## Prompt I gave
Go step by step. First only load movie_ratings.csv in Streamlit and prove the file is readable.

## What the AI produced
A small app.py that reads ../data/movie_ratings.csv and shows row count, column names, and the first 10 rows. (An earlier full 4-chart version was pulled back so we could go one step at a time.)

## What I changed and why
- Left the CSV in `data/` (copy of the course file)
- Put the app in `exercise/`
- Did not add charts yet

## Prompt (Question 1 only)
Answer Question 1 from the assignment using movie_ratings.csv: genre distribution among movies that were rated. Explain multi-genre handling first. Do not use a pie chart. Sort the bars. Stop after this one chart.

## What the AI produced
Horizontal bar chart of distinct rated movies per genre. Genres split on `|` then exploded. Count is movies, not ratings.

## What I changed and why
- Did not add Questions 2–4 yet (going one question at a time)
- Skipped pie chart because there are ~18 genres

## Prompt (Question 2)
Which genres have the highest average rating? Which have the lowest?

## What the AI produced
Sorted horizontal bar of mean rating per genre after exploding `|`. Highest and lowest called out. Mean is over ratings, not over movies.

## What I changed and why
- Still no Questions 3–4
- Chose rating-level mean (every star a user gave) rather than averaging movie averages first

## Prompt (Question 3)
How has the mean rating changed across movie release years?

## What the AI produced
Line chart of mean rating vs `year` (release year). Explicitly not `rating_year`. Missing years dropped.

## What I changed and why
- Still no Question 4
- Y-axis 0–5 so the trend is not visually exaggerated

## Prompt (Question 4)
Top 5 best-rated movies with a floor of 50 ratings, then 150.

## What the AI produced
Two sorted horizontal bars (50 vs 150) plus a slider for other floors. Rank by mean rating, then rating count.

## What I changed and why
- Show 50 and 150 side by side so the “what changes” question is visible without guessing
- Slider is the first interactive widget the assignment asked for

## Chart decisions (Abel)
- Q1 genre breakdown: horizontal bar, sorted
- Q2 genre satisfaction: vertical bar, sorted
- Q3 ratings over time: line (release year)
- Q4 best movies with a floor: horizontal bar, sorted

Q2 was switched from horizontal to vertical to match that decision. Q1, Q3, Q4 already matched.
