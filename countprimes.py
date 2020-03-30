#COUNT NO:OF PRIMES INCLUDING THE NUMBER?

def countprimes(num):
    if num < 2:  #for numbers 0,1
        return 0
    primes=[2]  # for number 2
    x=3 #for number greater than 2 
    while x <= num:
        for y in range(3,x,2): #checks number is prime or not
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return(len(primes))
    
    countprimes(100)
    
 #output:
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        25
