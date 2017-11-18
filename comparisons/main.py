from euclidean import distance
from Pearson import pearsonCoefficient
from recommendations import *

from data.critics import critics

# example
print(distance(critics, 'Lisa Rose', 'Gene Seymour'))
print(pearsonCoefficient(critics, 'Lisa Rose', 'Gene Seymour'))
print(topMatches(critics, 'Toby',num=3))
print(topMatches(critics, 'Toby',num=3, compare=distance))

print(getRec(critics, 'Toby', compare=pearsonCoefficient))
