"""

In a city-state of n people, there is a rumor going around that one of the n 

people is a spy for the neighboring city-state.

The spy, if it exists:

Does not trust anyone else.
Is trusted by everyone else (he's good at his job).
Works alone; there are no other spies in the city-state.
You are given a list of pairs, trust. Each trust[i] = [a, b] represents the fact 
that person a trusts person b.

If the spy exists and can be found, return their identifier. Otherwise, return -1.

"""

def uncover_spy(n, trust):
    
    people = []
    for i in range(1,n+1):
        people.append(i)
    
    table = {}
    for i in range(len(trust)):
        if trust[i][0] not in table:
            table[trust[i][0]] = [trust[i][1]]
        else:
            table[trust[i][0]].append(trust[i][1])
            
        if trust[i][0] in people:
            people.remove(trust[i][0])
    
    if len(people) == 1:
        for key,values in table.items():
            if people[0] not in values:
                return -1
    
        return people[0]
    
    return -1