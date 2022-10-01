import pandas as pd
import os
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from langdetect import detect


base_dir = os.path.dirname(__file__)
nlp = spacy.load("pl_core_news_md")
def detect_lang(name, description):
    return detect(name + " " + description)
def prepare_content(lang, name, description):
    if lang != "pl":
        return ""
    doc = nlp(name + " " + description)
    words = []
    for token in doc:
        if token.is_alpha and not token.is_stop:
            words.append(token.lemma_)
    return " ".join(words)

df = pd.read_json("https://zazepa.pl/download/datasets/books.json")
df = df.drop_duplicates(subset=["name"])
df["lang"] = df.apply(lambda row: detect_lang(row["name"], row["description"]), axis=1)
df["content"] = df.apply(lambda row: prepare_content(row["lang"], row["name"], row["description"]), axis=1)
documents = df[df["lang"] == "pl"]["name"]
documents.reset_index(inplace=True, drop=True)
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df[df["lang"] == "pl"]["content"])
features = vectorizer.get_feature_names_out()
cosine_sim = cosine_similarity(X, X)
final_df = pd.DataFrame(cosine_sim, columns = documents)
final_df = final_df.join(documents)