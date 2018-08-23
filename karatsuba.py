""" Karatsuba's Algorithm """
import time

def karatsuba(x,y):
    if x < 10 or y < 10:
        return x * y
    else:
        # Get the max size of x,y
        n = max(len(str(x)), len(str(y))) 
        m = n // 2
#        print(n,m)    
        # Split x and y
        a = x // 10**m
        b = x % 10**m
        c = y // 10**m
        d = y % 10**m
#        print(a,b,c,d) 
        # Compute the algorithms
        ac = karatsuba(a,c)
        bd = karatsuba(b,d)
        adbc = karatsuba(a+b,c+d) - ac - bd
        return (ac * 10**(2*m)) + (adbc * 10**(m)) + (bd)

def main():
    #print(karatsuba(23,56))
    #print(karatsuba(123,456))
    start = time.time()
    print(karatsuba(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627))
    end = time.time() - start   
    print(end)
main()
    
