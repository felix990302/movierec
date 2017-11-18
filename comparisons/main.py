from euclidean import distance
from Pearson import pearsonCoefficient
from recommendations import *
from transformer import *

from data.critics import critics
movies = flipPrefs(critics)

# example
"""
print(distance(critics, 'Lisa Rose', 'Gene Seymour'))
print(pearsonCoefficient(critics, 'Lisa Rose', 'Gene Seymour'))
print()
print(topMatches(critics, 'Toby',num=3))
print(topMatches(critics, 'Toby',num=3, compare=distance))
print()
print(getRec(critics, 'Toby', compare=pearsonCoefficient))
print()
"""
print(movies)
print(topMatches(movies, 'Superman Returns'))

