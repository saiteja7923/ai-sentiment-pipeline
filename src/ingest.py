import os
import tweepy
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime, timezone

# Load BEARER_TOKEN from .env
load_dotenv()
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

# Initialize Tweepy Client
client = tweepy.Client(bearer_token=BEARER_TOKEN, wait_on_rate_limit=True)

# Smart search query for relevant AI tweets
query = '"artificial intelligence" OR "generative AI" OR #AI lang:en -is:retweet'

# Path to tweet storage
DATA_PATH = "data/tweets.csv"

def get_last_timestamp(path):
    """Return latest tweet timestamp in UTC ISO format, or None if file doesn't exist"""
    if os.path.exists(path):
        df = pd.read_csv(path)
        if not df.empty:
            latest_date = pd.to_datetime(df["date"]).max()
            return latest_date.astimezone(timezone.utc).isoformat()
    return None

def fetch_tweets(query, max_results=10, existing_path=DATA_PATH):
    tweets = []

    # Determine start time based on most recent tweet saved
    start_time = get_last_timestamp(existing_path)
    print(f"📅 Fetching tweets after: {start_time or 'start of recent window'}")

    # Call Twitter API
    response = client.search_recent_tweets(
        query=query,
        tweet_fields=['id', 'created_at', 'author_id', 'text'],
        max_results=max_results,
        start_time=start_time  # only fetch newer tweets
    )

    # Parse results
    if response.data:
        for tweet in response.data:
            tweets.append({
                "id": tweet.id,
                "date": tweet.created_at,
                "user_id": tweet.author_id,
                "content": tweet.text
            })

        new_df = pd.DataFrame(tweets)

        # Combine with existing tweets and deduplicate
        if os.path.exists(existing_path):
            existing_df = pd.read_csv(existing_path)
            combined_df = pd.concat([existing_df, new_df]).drop_duplicates(subset='id', keep='last')
        else:
            combined_df = new_df

        os.makedirs("data", exist_ok=True)
        combined_df.to_csv(existing_path, index=False)
        print(f"✅ New tweets saved: {len(new_df)}")
        print(f"📊 Total tweets in dataset: {len(combined_df)}")
    else:
        print("⚠️ No new tweets found.")

if __name__ == "__main__":
    fetch_tweets(query)
