# Część III Przepisy
## Rozdział 11 Słów kilka o przetwarzaniu języka naturalnego
### Wymagane pakiety

pip install spacy
pip install goose3
python -m spacy download pl_core_news_sm
pip install wordcloud
pip install matplotlib

python -m spacy download pl_core_news_md
python -m spacy download pl_core_news_lg

pip install scikit-learn

### Uruchamianie scraper'ów

+ listing_11_1.py - **scrapy runspider listing_11_1.py -o urls.csv -t csv**
