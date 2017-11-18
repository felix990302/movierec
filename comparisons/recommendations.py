# comparisons/recommendations
from Pearson import pearsonCoefficient

def topMatches(prefs, name, num=5 ,compare=pearsonCoefficient):
    scores=[(compare(prefs,name,other),other)
            for other in prefs if other!=name]

    scores.sort(reverse=True)
    return scores[:num]


def getRec(prefs,name,compare=pearsonCoefficient):
    totals={}
    simSums={}
    for other in prefs:
        print("totals:", totals)
        print("simSums:", simSums)
        if other==name:continue
        sim = compare(prefs,name,other)

        if sim<=0:continue
        for item in prefs[other]:

            if item not in prefs[name] or prefs[name][item]==0:
                totals.setdefault(item,0)

                totals[item]+=prefs[other][item]*sim

                simSums.setdefault(item,0)
                print(sum)
                simSums[item]+=sim

    rankings = [(total/simSums[item],item) for item,total in totals.items()]

    rankings.sort(reverse=True)
    return rankings