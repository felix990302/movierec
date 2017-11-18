
def flipPrefs(prefs):
    result={}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item,{})
            #flip item and person
            result[item][person]=prefs[person][item]
    return result



