#Write the program if the list of integers has 007 in order return TRUE else FALSE?

def spygame(nums):
    code = [0,0,7,'x']
    for num  in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1
    
 spygame([1,2,4,0,0,7,5])
 spygame([1,0,2,4,0,5,7])
 spygame([1,7,2,0,4,5,0])
 
 #output: TRUE
          TRUE
          FALSE
