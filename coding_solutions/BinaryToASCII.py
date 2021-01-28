"""

Given a binary string (ASCII encoded), write a function that returns the 

equivalent decoded text.

Every eight bits in the binary string represents one character on the ASCII 

table.

"""

def csBinaryToASCII(binary):
    character_list = []
    ans = ''
    for i in range(0,len(binary),8):
        character_list.append(int(binary[i:i+8],2))
    
    for num in character_list:
        ans += chr(num)
        
    return ans