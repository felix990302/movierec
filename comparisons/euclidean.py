# comparison/__init__.py

from math import sqrt


# Returns a distance-based similarity score for person1 and person2
def distance(prefs, person1, person2):
    sum = 0

    for item in prefs[person1]:
        if item in prefs[person2]:
            sum += (prefs[person1][item] - prefs[person2][item]) ** 2

    # Add up the squares of all the differences

    return 1 / (1 + sqrt(sum))
