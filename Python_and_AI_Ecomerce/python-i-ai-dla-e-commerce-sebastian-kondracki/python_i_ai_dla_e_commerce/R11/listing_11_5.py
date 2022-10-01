import spacy

nlp = spacy.load("pl_core_news_sm")
txt = "Zastanawiasz się, czy sweter wełniany możesz założyć do pracy? Odpowiadamy: Tak! W połączeniu z elegancką spódnicą czy np. stylowymi spodniami typu cygaretki będziesz wyglądać naprawdę szykownie i bardzo stylowo."
doc = nlp(txt)
sentences = list(doc.sents)
for sentece in sentences:
    print(sentece)