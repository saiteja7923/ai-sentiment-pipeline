import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Path to sentiment-analyzed tweets
DATA_PATH = "data/tweets_with_sentiment.csv"

@st.cache_data
def load_data(path):
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        st.error(f"Data file not found at {path}. Please run the pipeline to generate data.")
        return pd.DataFrame()

df = load_data(DATA_PATH)

if not df.empty:
    # Page title
    st.title("🤖 AI Tweet Sentiment Dashboard")
    st.markdown("Analyze public perception of Artificial Intelligence using real-time tweets.")

    # Sidebar filters
    sentiment_filter = st.sidebar.multiselect(
        "Filter by Sentiment", 
        options=df["sentiment"].unique(),
        default=df["sentiment"].unique()
    )

    # Filter dataframe based on selection
    filtered_df = df[df["sentiment"].isin(sentiment_filter)]

    # Show total and filtered tweet counts
    st.markdown(f"### Total tweets analyzed: {len(df)}")
    st.markdown(f"### Tweets after filter: {len(filtered_df)}")

    # Sentiment distribution bar chart
    st.subheader("📊 Sentiment Distribution")
    sentiment_counts = filtered_df["sentiment"].value_counts().sort_index()

    fig, ax = plt.subplots()
    sentiment_df = sentiment_counts.reset_index()
    sentiment_df.columns = ['sentiment', 'count']
    sns.barplot(data=sentiment_df, x="sentiment", y="count", hue="sentiment", palette="coolwarm", legend=False, ax=ax)
    ax.set_ylabel("Number of Tweets")
    ax.set_xlabel("Sentiment")
    ax.set_ylim(0, max(sentiment_counts.values) * 1.1)  # add some padding on y-axis
    st.pyplot(fig)

    # Sample tweets display
    st.subheader("💬 Sample Tweets")
    num_samples = st.slider("Number of tweets to show", min_value=1, max_value=len(filtered_df), value=5)
    st.write(filtered_df[["date", "sentiment", "content"]].head(num_samples))

    # Word Cloud visualization
    st.subheader("☁️ Word Cloud")
    if len(sentiment_counts) > 0:
        selected_wc_sentiment = st.selectbox("Select sentiment for Word Cloud", sentiment_counts.index)
        text = " ".join(filtered_df[filtered_df["sentiment"] == selected_wc_sentiment]["clean_content"].dropna())
        if text.strip():
            wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
            fig_wc, ax_wc = plt.subplots(figsize=(10, 5))
            ax_wc.imshow(wordcloud, interpolation="bilinear")
            ax_wc.axis("off")
            st.pyplot(fig_wc)
        else:
            st.info("No text data available for the selected sentiment to generate a word cloud.")
    else:
        st.info("No sentiments found to generate word cloud.")
else:
    st.warning("No tweet data available to display.")
# Footer