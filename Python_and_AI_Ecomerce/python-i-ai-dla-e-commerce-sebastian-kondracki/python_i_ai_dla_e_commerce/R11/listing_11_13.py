from sklearn.feature_extraction.text import TfidfVectorizer
import spacy
import pandas as pd
nlp = spacy.load("pl_core_news_md")

corpus = [
    "Programowanie sterowane testami w Python",
    "Python i sygnały",
    "Praktycznie i po ludzku o prawie w IT",
    "Projekt IT od przygotowania strategii zakupowej do negocjacji umowy wdrożeniowej",
]

corpus_basic_form = []
for line in corpus:

    doc = nlp(line)
    words = []
    for token in doc:
        if token.is_alpha and not token.is_stop:
            words.append(token.lemma_)
    corpus_basic_form.append(" ".join(words))
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus_basic_form)
features = vectorizer.get_feature_names_out()
print(corpus_basic_form)
print(features)
print(X)
df = pd.DataFrame(X[0].T.todense(), index=features, columns=["tf-idf"])
df = df.sort_values(by=["tf-idf"], ascending=False)
print(df)