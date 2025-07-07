from src.ingest import fetch_tweets
from src.clean import clean_tweets_from_csv
from src.analyze_sentiment import analyze_sentiment

# Define the smart query globally
query = '"artificial intelligence" OR "generative AI" OR #AI lang:en -is:retweet'

def main():
    print("\nStarting tweet ingestion...")
    fetch_tweets(query=query, max_results=10)

    print("\nCleaning tweets...")
    clean_tweets_from_csv()

    print("\nRunning sentiment analysis...")
    analyze_sentiment()

if __name__ == "__main__":
    main()
