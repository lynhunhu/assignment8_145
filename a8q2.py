#Name: Nhu Nhu Ly
#NSID: cvd326
#instructor's name: Eric Neufeld
#student number: 11333935
#course number: 27177
#lab section: Monday 1:30 - 2:50 - 28623


def Fib(n): #starting from 0 so 0 would be the 0th Fibonacci number in the sequence
    if n < 0: 
        print("Please enter a positive number")
        return None
    if n <= 1:
        return n
    else:
        return(Fib(n-1) + Fib(n-2))

def Moos(n):
    if n < 0: 
        print("Please enter a positive number")
    if n <= 2:
        return n
    else:
        return(Moos(n-1) + Moos(n-2) + Moos(n-3))

def substr(c, r, s):
    if s == '':
        return ''

    elif s[0] == c:
        return r + str(substr(c,r,s[1:]))

    return s[0] + str(substr(c,r,s[1:]))





