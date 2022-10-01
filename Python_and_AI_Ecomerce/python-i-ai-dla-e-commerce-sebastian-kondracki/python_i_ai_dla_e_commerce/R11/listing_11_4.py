import spacy
from spacy.lang.pl.examples import sentences

nlp = spacy.load("pl_core_news_sm")
doc = nlp(sentences[0])
print(doc.text)
for token in doc:
    print(token.text, token.pos_, token.dep_)