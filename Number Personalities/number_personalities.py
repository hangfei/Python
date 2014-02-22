#main method
def main():
    limit = 100    #limit can change
    n=1
    #in the while loop, call each method to print
    while n <= limit:
        print n,
        if is_prime(n):
            print "prime,",
        else:
            print "composite,",
        #would the loop stop if I use else?

        if is_happy(n):
            print "happy,",
        else:
            print "unhappy,",

        if is_triangular(n):
            print "triangular,",
        else:
            print "not triangular,",

        if is_square(n):
            print "square,",
        else:
            print "not square,",

        if is_smug(n):
            print "smug,",
        else:
            print "not smug,",

        if is_honest(n):
            print "hoest"
        else:
            print "not honest"

        #go to next cycle and change n
        n += 1


#happy
def is_happy(m):
    cycle = 0
    continuity = 1
    n = 0
    while True:
        if continuity == 0:
            cycle = 0
        continuity = 1
        n = (m % 10) ** 2
        while True:
            m = m/10
            n = n + (m %10) ** 2
            if m < 10:
                break
        m = n    
        if n == 1:
            return True
        elif n == 4 and cycle == 0:
            cycle += 1
        elif n == 16 and cycle == 1:
            cycle += 1
        elif n == 37 and cycle ==2:
            cycle += 1
        elif n == 58 and cycle ==3 :
            cycle += 1
        elif n == 89 and cycle == 4:
            cycle += 1
        elif n == 145 and cycle == 5:
            cycle += 1
        elif n == 42 and cycle == 6:
            cycle +=1
        elif n == 20 and cycle == 7:
            return False
        else:
            continuity = 0



            


#prime
def is_prime(n):
    i = 1
    t = 0
    while i != n+1:
        if n % i ==0:
            t += 1
        i += 1
    return t == 2





def is_triangular(n):
    "To tell whether it's a triangular number"
    t = 0
    i=1
    while t < n:
        t = t + i
        i += 1
        if t == n:
            return True
        elif t > n:
            return False
        else:            
            pass
        

#square
def is_square(n):
    "to tell whether a number is a square number"
    i=0
    while i < n:
        i += 1
        if n == i*i:
            return True
        elif i >= n:
            return False
        


#smug
def is_smug(n):
    for i in range(1,n):
        j=0
        while j <= n:
            j += 1
            if n == (i * i + j * j):                
                return True
            
    return False





#honest
def is_honest(n):
    k = 0
    while k < n:
        k += 1
        if (n/k) == k and n != 1:
            if not is_square(n):
                return True

    



######
if __name__ == "__main__":
  main()
