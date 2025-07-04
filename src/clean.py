import os
import pandas as pd
import re

# Get the project root directory (one level up from this script's folder)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define input and output file paths
input_path = os.path.join(BASE_DIR, "data", "tweets.csv")
output_path = os.path.join(BASE_DIR, "data", "clean_tweets.csv")

def clean_tweet(text):
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)

    # Remove user @ mentions
    text = re.sub(r'@\w+', '', text)

    # Remove hashtags (if you want to keep hashtags, comment this line)
    text = re.sub(r'#\w+', '', text)

    # Remove emojis and special chars (keep only letters, numbers, and basic punctuation)
    text = re.sub(r'[^\w\s.,!?\'"]+', '', text)

    # Lowercase
    text = text.lower()

    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    return text

def clean_tweets_from_csv(input_path=input_path, output_path=output_path):
    if not os.path.exists(input_path):
        print(f"❌ Input file not found: {input_path}")
        return

    df = pd.read_csv(input_path)
    print(f"Cleaning {len(df)} tweets...")

    df['clean_content'] = df['content'].apply(clean_tweet)

    df.to_csv(output_path, index=False)
    print(f"Cleaned tweets saved to {output_path}")

if __name__ == "__main__":
    clean_tweets_from_csv()
