from euclidean import distance
from Pearson import pearsonCoefficient

from data.recommendations import critics

# example
print(distance(critics, 'Lisa Rose', 'Gene Seymour'))
print(pearsonCoefficient(critics, 'Lisa Rose', 'Gene Seymour'))
