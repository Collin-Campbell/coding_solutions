"""

There are N students in a baking class together. Some of them are friends, while some 

are not friends. The students' friendship can be considered transitive. This means 

that if Ami is a direct friend of Bill, and Bill is a direct friend of Casey, Ami is 

an indirect friend of Casey. A friend circle is a group of students who are either 

direct or indirect friends.

Given a N*N matrix M representing the friend relationships between students in the 

class. If M[i][j] = 1, then the ith and jth students are direct friends with each 

other, otherwise not.

You need to write a function that can output the total number of friend circles 

among all the students.

"""

def csFriendCircles(friendships):
    
    queue = []
    count = 0
    
    for i in range(len(friendships)):
        for j in range(len(friendships[i])):
            if friendships[i][j] == 1:
                queue.append(friendships[i][j])
            if friendships[i][j] == 0 and len(queue) == 0:
                continue
            if friendships[i][j] == 0:
                queue.pop()
                if len(queue) == 0:
                    count += 1
    
    if count == 0:
        return 1
        
    return len(queue) + count