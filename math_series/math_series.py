
def Fibonacci(n): 
    if n<0: 
        
        print("Incorrect input") 
    elif n==0: 
        return 0
    elif n==1: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 

def lucas(n):

    if (n == 0) : 
        return 2
    if (n == 1) : 
        return 1
  
    
    return lucas(n - 1) + lucas(n - 2)


def sum_series(n, x=0 , y=1):
    if x == 0 and y== 1:
        return Fibonacci(n)
    elif x == 2 and y== 1:
        return lucas(n)
    else :
        return sum_series(n - 1, x, y) + sum_series(n - 2, x, y)
