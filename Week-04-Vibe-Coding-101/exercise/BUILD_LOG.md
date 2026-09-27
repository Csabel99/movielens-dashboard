# Week 4 Vibe Coding — build log (raw, not a writeup)

Where this lives: `Week-04-Vibe-Coding-101/exercise/BUILD_LOG.md`
Do not lose this file. Next week’s report needs the real process, not memory.

---

## Moment 1 — Getting the data in

**Prompt I gave (paraphrase of what I actually asked):**
I had the MovieLens CSV on the course GitHub (`CUNYTechPrep/ds-dev-fall-2026` → `Week-04-Vibe-Coding-101/data/movie_ratings.csv`). I asked whether to move it or leave it in `data`. I also asked to make an `exercise` folder.

**What the AI produced first:**
Wanted to start writing the whole dashboard immediately. Also suggested copying the CSV into my own project because Streamlit Cloud cannot read the course repo.

**What I changed and why:**
- Left the original on the course GitHub. Copied CSV into my project: `Week-04-Vibe-Coding-101/data/movie_ratings.csv`.
- Did not add an `exercise` folder on the course repo (I can’t / shouldn’t).
- Told the AI to slow down after it generated all 4 charts at once.

---

## Moment 2 — The 4 questions / chart choices

**Prompt I gave:**
The 4 assignment questions, one at a time. Then: “summarize each 4 questions because I need to make a decision which chart for each.” Then I picked from the toolkit table.

**What the AI produced on the first try:**
A full 4-chart Streamlit app in one shot (horizontal bars for Q1/Q2/Q4, line for Q3, plus a pie-chart warning for genres). I made it rewind to step-by-step.

**What I changed and why (my chart decisions):**
- Q1 Genre breakdown → horizontal bar, sorted. Not pie (18 genres).
- Q2 Genre satisfaction → I changed this to a **vertical** bar, sorted. AI first used horizontal.
- Q3 Ratings over time → line. Use `year` (release), not `rating_year`.
- Q4 Best movies with a floor → horizontal bar, 50 vs 150 side by side + slider. I asked if Q4 could be a heatmap; I did **not** use heatmap (only one category + a ranking, not two categories).

**AI counting choices I left in (to judge later):**
- Multi-genre: split `genres` on `|` then explode. A movie like Crime|Drama counts in both.
- Q1 counts **movies**, not ratings.
- Q2/Q3/Q4 mean = mean of **ratings**.

---

## Moment 3 — GitHub + Streamlit deploy

**Prompt I gave:**
Task 2 deploy. First time. Go slow. Then: root `app.py` (option B) vs nested path.

**What the AI produced:**
Git init, commit, public repo `https://github.com/Csabel99/movielens-dashboard`, Streamlit Cloud from `main`.

**What I changed and why:**
- Chose option B: moved `app.py` to the **repo root** so the Streamlit “Main file path” can just be `app.py` like the handout.
- CSV stayed in `Week-04-Vibe-Coding-101/data/`.
- App is live; I can see all 4 questions and charts.

---

## Extra scraps (keep)

- Cursor, not Codespaces. Streamlit Cloud only builds from GitHub.
- Widgets: rating-count floor slider (assignment asked for 1–2).
- Submission this week is the public Streamlit URL, not this log. This log is for NEXT week.
