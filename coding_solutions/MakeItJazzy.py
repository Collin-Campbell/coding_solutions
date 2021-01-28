"""

Create a function that concatenates the number 7 to the end of every chord in 

a list. If a chord already ends with a 7, ignore that chord.

"""

def csMakeItJazzy(chords):
    ans = []
    for chord in chords:
        if chord[len(chord)-1] != '7':
            ans.append(chord + '7')
        else:
            ans.append(chord)
    
    return ans