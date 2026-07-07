import pandas as pd
import re
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# Load Dataset
df = pd.read_csv("cyberbullying_tweets.csv")


# Select columns
df = df[[
    "tweet_text",
    "cyberbullying_type"
]]


# Remove missing
df = df.dropna()


# Clean text
def clean(text):

    text = str(text).lower()

    text = re.sub(
        r"[^a-z ]",
        "",
        text
    )

    return text


df["tweet_text"] = (
    df["tweet_text"]
    .apply(clean)
)


X = df["tweet_text"]

y = df["cyberbullying_type"]


# Split
X_train, X_test, y_train, y_test = (
    train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )
)


# Pipeline
model = Pipeline([

(
"tfidf",

TfidfVectorizer(
max_features=10000,
ngram_range=(1,2),
stop_words="english"
)

),

(
"model",

LogisticRegression(
max_iter=1000
)

)

])


# Train
model.fit(
X_train,
y_train
)


# Accuracy
pred = model.predict(
X_test
)

print(
"Accuracy:",
accuracy_score(
y_test,
pred
)
)


# Save
joblib.dump(
model,
"model.pkl"
)

print(
"Model Saved"
)