import spacy
import os
from wordcloud import WordCloud
     
nlp = spacy.load("pl_core_news_sm")

base_dir = os.path.dirname(__file__)
txt_dir = os.path.join(base_dir, "txt")
img_dir = os.path.join(base_dir, "img")
os.makedirs(img_dir, exist_ok=True)
txt_files = [f for f in os.listdir(txt_dir) if os.path.isfile(os.path.join(txt_dir, f))]

for txt_file in txt_files:
    with open(os.path.join(txt_dir, txt_file), "r") as file:
        txt = file.read().replace("\n", "")
    doc = nlp(txt)
    words = []
    for token in doc:
        if token.is_alpha and not token.is_stop and token.pos_ == "NOUN": 
            words.append(token.lemma_)
    wc = WordCloud(max_font_size=40, background_color="white").generate(" ".join(words))
    img_file = txt_file.replace(".txt", ".png")
    wc.to_file(os.path.join(img_dir, img_file))
    print("Chmurka {} wygenerowana pomyślnie!".format(img_file))