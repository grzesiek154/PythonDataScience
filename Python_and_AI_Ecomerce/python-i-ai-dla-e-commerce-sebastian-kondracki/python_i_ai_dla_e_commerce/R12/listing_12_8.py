from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.model_selection import train_test_split
import spacy
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

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
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)
features = vectorizer.get_feature_names_out()
clf = MultinomialNB().fit(X_train, y_train)
y_pred = clf.predict(X_test)

new_email = clean_lemma('Poprawcie wyszukiwarke ledwo działa')
X_new_email = vectorizer.transform([new_email])
print(new_email)
y_pred_new_email = clf.predict(X_new_email)
y_probs = clf.predict_proba(X_new_email)
print(y_pred_new_email)
print(y_probs)