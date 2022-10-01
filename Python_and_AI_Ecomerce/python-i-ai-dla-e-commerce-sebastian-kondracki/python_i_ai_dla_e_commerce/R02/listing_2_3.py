import Levenshtein

name1 = 'Sebastian'
name2 = 'Sebastyan'
name3 = 'Seweryn'
print('Odległość Levenshteina Sebastian vs Sebastyan:',
Levenshtein.distance(name1, name2))
print('Odległość Levenshteina Sebastian vs Seweryn:',
Levenshtein.distance(name1, name3))