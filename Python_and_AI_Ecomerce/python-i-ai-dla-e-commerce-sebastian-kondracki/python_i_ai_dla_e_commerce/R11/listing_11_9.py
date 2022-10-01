import spacy
import pandas as pd

nlp = spacy.load("pl_core_news_sm")
txt = """Joanna Koroniewska na Instagramie opublikowała zdjęcie w jednym
      z najmodniejszych modeli sukienek na jesień 2021. Skórzane sukienki to
      mocny trend! Wyglądają elegancko i bardzo kobieco. Model, która ma na
      sobie Joasia możecie zamówić na Bonprix, ale znalazłyśmy dla was
      również alternatywy z Sinsay i Reserved. (20 października 2021)"""

doc = nlp(txt)
rows = []
if doc.ents:
    for ent in doc.ents:
        rows.append({
            "text": ent.text,
            "start": ent.start_char,
            "end": ent.end_char,
            "label": ent.label_,
        })
df = pd.DataFrame(rows)
print(df)
