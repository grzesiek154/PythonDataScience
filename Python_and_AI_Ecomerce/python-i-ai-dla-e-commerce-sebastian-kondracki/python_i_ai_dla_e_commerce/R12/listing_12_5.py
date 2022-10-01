import pandas as pd
from sklearn.model_selection import train_test_split
import spacy

nlp = spacy.load("pl_core_news_sm")
url = "https://zazepa.pl/download/datasets/emails.csv"
df = pd.read_csv(url)
def clean_lemma(s):
    doc = nlp(s)
    words = []
    for token in doc:
        if token.is_alpha and not token.is_stop:
            words.append(token.lemma_)
    return " ".join(words)
X = df["subject"].apply(clean_lemma) + " " + df["message"].apply(clean_lemma)
y = df["category"]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
print("Rozmiar zbioru treningowego", len(X_train))
print("Rozmiar zbioru testowego", len(X_test))