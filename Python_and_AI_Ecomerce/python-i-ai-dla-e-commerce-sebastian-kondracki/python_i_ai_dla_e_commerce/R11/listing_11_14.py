import os
import json
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

analyzed_files = {}
base_dir = os.path.dirname(__file__)
with open(os.path.join(base_dir, "analyzed_files.json"), "r", encoding="UTF-8") as json_file:
    analyzed_files = json.load(json_file)
docs = [row["words"] for row in analyzed_files.values()]
docs_name = [key for key in analyzed_files.keys()]
vectorizer = TfidfVectorizer(smooth_idf=False, use_idf=True, ngram_range=(1, 1))
X = vectorizer.fit_transform(docs)
features = vectorizer.get_feature_names_out()
for index, result in enumerate(X):
    df = pd.DataFrame(result.T.todense(), index=features, columns=["tf-idf"])
    df = df.sort_values(by=["tf-idf"], ascending=False)
    analyzed_files[docs_name[index]]["keywords"] = df.head(5).index.tolist()
df_tf_idf_bow = pd.DataFrame(data=X.toarray(), index=docs_name, columns=features)
df_tf_idf_bow.to_csv(os.path.join(base_dir, "bow.csv"))
print("Bag of words zapisany!")
with open(os.path.join(base_dir, "analyzed_files.json"), "w", encoding="UTF-8") as json_file:
    json.dump(analyzed_files, json_file, indent=4, sort_keys=True, ensure_ascii=False)
print("Plik analyzed_files.json zaktualizowany!")
