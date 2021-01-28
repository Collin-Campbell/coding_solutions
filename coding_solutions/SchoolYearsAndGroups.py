"""

Imagine a school that children attend for years. In each year, there are a 

certain number of groups started, marked with the letters. So if years = 7 

and groups = 4For the first year, the groups are 1a, 1b, 1c, 1d, and for the 

last year, the groups are 7a, 7b, 7c, 7d.

Write a function that returns the groups in the school by year (as a string), 

separated with a comma and space in the form of "1a, 1b, 1c, 1d, 2a, 2b 

(....) 6d, 7a, 7b, 7c, 7d".

"""

def csSchoolYearsAndGroups(years, groups):
    ans = ''
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for num in range(1,years+1):
        for letter in letters[:groups]:
            ans += (str(num) + letter + ', ')
    
    return ans.strip(', ')