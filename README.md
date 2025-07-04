# AI Tweet Sentiment Pipeline

This project collects, cleans, analyzes, and visualizes real-time tweets related to **Artificial Intelligence (AI)** using Python. It automatically fetches new tweets every day and updates the sentiment dashboard.

## Workflow Overview
main.py
│
├── src/
│ ├── ingest.py # Pulls new tweets using Twitter API
│ ├── clean.py # Cleans and preprocesses tweet text
│ └── analyze_sentiment.py # Performs sentiment analysis using NLTK's VADER
│
├── data/
│ ├── tweets.csv # Raw tweets
│ ├── clean_tweets.csv # Cleaned text
│ └── tweets_with_sentiment.csv # Final output with sentiment
│
└── streamlit_app.py # Interactive dashboard with filters and visualizations

## Features

- Fetches tweets related to `"artificial intelligence"`, `"generative AI"`, or `#AI`
- Automatically deduplicates previously seen tweets
- Cleans tweet content using regex
- Applies sentiment analysis using VADER (Positive, Neutral, Negative)
- Visualizes results in a Streamlit dashboard with:
  - Sentiment breakdown chart
  - Filtered tweet viewer
  - Word cloud
