# AI Tweet Sentiment Pipeline

This project collects, cleans, analyzes, and visualizes real-time tweets related to **Artificial Intelligence (AI)** using Python. It automatically fetches new tweets every day and updates the sentiment dashboard.

## Workflow Overview

## Features

- Fetches tweets related to `"artificial intelligence"`, `"generative AI"`, or `#AI`
- Automatically deduplicates previously seen tweets
- Cleans tweet content using regex
- Applies sentiment analysis using VADER (Positive, Neutral, Negative)
- Visualizes results in a Streamlit dashboard with:
  - Sentiment breakdown chart
  - Filtered tweet viewer
  - Word cloud
