# for i in range(1,11,2):
#     print(i)

# for a in "kolkata":
#     print(a)
    

def fib(m):
    if m == 0 or m ==1:
        return 1
    else:
        return fib(m-1) + fib(m-2)
        
        
print(fib(12))