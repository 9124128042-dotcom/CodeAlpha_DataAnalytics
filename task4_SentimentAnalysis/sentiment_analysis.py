import pandas as pd
from textblob import TextBlob

# Load data
df = pd.read_csv("../Task3_DataVisualization/quotes.csv")

# Function to get sentiment
def get_sentiment(text):
    analysis = TextBlob(str(text))
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment
df["Sentiment"] = df["Quote"].apply(get_sentiment)

# Show result
print(df.head())

# Save output
df.to_csv("sentiment_output.csv", index=False)

print("Sentiment analysis completed!")