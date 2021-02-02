"""

Given a list of different students' scores, write a function that returns the 

average of each student's top five scores. You should return the averages in 

ascending order of the students' id numbers.

Each entry (scores[i]) has the student's id number (scores[i][0]) and the student's 

score (scores[i][1]). The averages should be calculated using integer division.

"""

def csAverageOfTopFive(scores):
    
    table = {}
    for i in range(len(scores)):
        for j in range(1,len(scores[i])):
            if scores[i][0] not in table:
                table[scores[i][0]] = []
                table[scores[i][0]].append(scores[i][j])
            else:
                table[scores[i][0]].append(scores[i][j])
    
    ans = []
    
    for student,scores in table.items():
        total_score = 0
        number_of_scores = 0
        top_five = len(scores) if len(scores) <= 5 else 5
        for i in range(top_five):
            total_score += sorted(scores,reverse=True)[i]
            number_of_scores += 1
        student_average = (total_score // number_of_scores)
        ans.append([student,student_average])
                
    return ans