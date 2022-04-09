from itertools import permutations
from typing import Dict, List, Tuple

# (the difference in lengths of the name and the country) multiplied by 
# (the number of unique letters shared between their name and the country's name
places: List[str] = 'Afghanistan, Bangladesh, Guatemala, Indonesia, Liechtenstein, Luxembourg, Mauritania, Montenegro, Switzerland, Turkmenistan'.lower().replace(' ', '').split(',')
names: List[str] = 'Alexandra, Benjamin, Catherine, Dominic, Eleanor, Fernando, Gabrielle, Harrison, Isabella, Jeremiah'.lower().replace(' ', '').split(',')
scores: Dict[Tuple[str, str], int] = dict()

for place in places:
    for name in names:
        scores[(place, name)] = abs(len(place) - len(name))*len(set(place).intersection(set(name)))


best_score: int = 0
best_places_ordering: List[str] = places

count = 0
for place_ordering in permutations(places, len(places)):
    count += 1
    score = 0
    for i in range(len(place_ordering)):
        score += scores[(place_ordering[i], names[i])]
    if score > best_score:
        best_score = score
        best_places_ordering = list(place_ordering)

print(best_places_ordering)
