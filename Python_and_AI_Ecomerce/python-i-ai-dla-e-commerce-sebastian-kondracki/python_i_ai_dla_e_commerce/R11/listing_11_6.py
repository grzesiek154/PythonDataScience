import spacy
import pandas as pd

nlp = spacy.load("pl_core_news_sm")
txt = """Skórzana galanteria to kolejna obowiązkowa pozycja, zaliczana
do klasyki najbardziej eleganckich prezentów dla mężczyzny. Jeżeli
szukasz więc szukać czegoś jednocześnie stylowego, ale i praktycznego,
postaw na markowy skórzany pasek. To podstawa męskiej garderoby, która
sprawdzi się zarówno w stroju formalnym, jak i w wielu casualowych
stylizacjach. Skórzany pasek jest jak krawat. Przynajmniej jeden
powinien znaleźć się w garderobie dorosłego faceta."""

doc = nlp(txt)
rows = []
for token in doc:
    rows.append({
        "token": token,
        "pos": token.pos_,
        "lemma": token.lemma_,
        "stop": token.is_stop,
        "shape": token.shape_,
    })

df = pd.DataFrame(rows)
print(df)
