import os
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# # Download VADER lexicon if not already present
# nltk.download('vader_lexicon')

# Get paths relative to project structure
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_path = os.path.join(BASE_DIR, "data", "clean_tweets.csv")
output_path = os.path.join(BASE_DIR, "data", "tweets_with_sentiment.csv")

def classify_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(text)["compound"]
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def analyze_sentiment():
    if not os.path.exists(input_path):
        print(f"❌ Cleaned tweet file not found: {input_path}")
        return

    df = pd.read_csv(input_path)
    print(f"🔍 Running sentiment analysis on {len(df)} tweets...")

    df["sentiment"] = df["clean_content"].apply(classify_sentiment)
    df.to_csv(output_path, index=False)

    print(f"✅ Sentiment analysis complete. Results saved to: {output_path}")

if __name__ == "__main__":
    analyze_sentiment()
