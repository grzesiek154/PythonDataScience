from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.model_selection import train_test_split
import spacy
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import numpy as np
import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
from time import time

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
X_train, X_test, y_train, y_test = train_test_split(X, y,
random_state=42)
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)
features = vectorizer.get_feature_names_out()
t = time()
clf = MultinomialNB().fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Czas trenowania i testowania {:0.3f} s".format(float(time() - t)))
print(accuracy_score(y_test, y_pred))
unique_label = np.unique([y_test, y_pred])
df_cm = pd.DataFrame(
    confusion_matrix(y_test, y_pred, labels=unique_label),
    index=["true:{:}".format(x) for x in unique_label],
    columns=["pred:{:}".format(x) for x in unique_label],
)
print(df_cm)
sn.set(font_scale=0.7)
sn.heatmap(df_cm, annot=True, annot_kws={"size": 8})
plt.show()