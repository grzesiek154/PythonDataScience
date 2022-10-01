import spacy
import pandas as pd
from spacy import displacy

nlp = spacy.load("pl_core_news_sm")
txt = """Joanna Koroniewska na Instagramie opublikowała zdjęcie w jednym
z najmodniejszych modeli sukienek na jesień 2021. Skórzane sukienki to
mocny trend! Wyglądają elegancko i bardzo kobieco. Model, która ma na
sobie Joasia możecie zamówić na Bonprix, ale znalazłyśmy dla was
również alternatywy z Sinsay i Reserved. (20 października 2021)"""

doc = nlp(txt)
rows = []
html = ""

if doc.ents:
    for ent in doc.ents:
        rows.append({
            "text": ent.text,
            "start": ent.start_char,
            "end": ent.end_char,
            "label": ent.label_,
        })
    html = displacy.render(doc, style="ent", jupyter=False, page=True)

df = pd.DataFrame(rows)
with open("ents.html", "w") as f:
    f.write(html)
print(df)