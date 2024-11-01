# make the letter j out of "x" characters of n size

def makeLetterJ(n):
    for i in range (0,n):
        if i == 0:
            print("x "*(n-1))
        elif i < n-1:
            print(" "*(n-2) + "x ")
        else: print("x "*round(n/2))
makeLetterJ(10)
        