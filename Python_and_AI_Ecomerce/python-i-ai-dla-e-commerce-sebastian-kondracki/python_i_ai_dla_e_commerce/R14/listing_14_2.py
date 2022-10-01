import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

df = pd.read_csv("https://zazepa.pl/download/datasets/items.csv", sep = ",")
itemsets = apriori(df, min_support = 0.0001, use_colnames = True).sort_values(by = ['support'], ascending = False)
rules = association_rules(itemsets, metric="lift")
print(rules[ (rules['lift'] > 6) & (rules['confidence'] >= 0.8)][["antecedents", "consequents", "confidence","support","lift"]])