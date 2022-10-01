import spacy
import os
import json

nlp = spacy.load("pl_core_news_md")
base_dir = os.path.dirname(__file__)
txt_dir = os.path.join(base_dir, "txt")
txt_files = [f for f in os.listdir(txt_dir) if
os.path.isfile(os.path.join(txt_dir, f))]
analyzed_files = {}

for txt_file in txt_files:
    with open(os.path.join(txt_dir, txt_file), "r") as file:
        txt = file.read().replace("\n", "")
    doc = nlp(txt)
    words = []
    nouns = []

    for token in doc:
        if token.is_alpha and not token.is_stop:
            words.append(token.lemma_)
        if token.is_alpha and not token.is_stop and token.pos_ == "NOUN":
            nouns.append(token.lemma_)
    ents = []
    if doc.ents:
        for ent in doc.ents:
            ent_item = {
                "text": ent.text,
                "start": ent.start_char,
                "end": ent.end_char,
                "label": ent.label_,
            }
            ents.append(ent_item)
    row = {
        "text": txt,
        "words": " ".join(words),
        "nouns": " ".join(nouns),
        "ents": ents,
    }
    analyzed_files[txt_file] = row
    print("Plik {} przeanalizowany!".format(txt_file))
      
with open(os.path.join(base_dir,"analyzed_files.json"), "w", encoding="UTF-8") as json_file:
    json.dump(analyzed_files, json_file, indent=4, sort_keys=True, ensure_ascii=False)