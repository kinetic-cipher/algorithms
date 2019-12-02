
# basic version
def fib_seq(N):
    F = [0]*N
    F[1] = 1  
    for n in range(2,N):
       F[n] = F[n-1]+F[n-2]
    return F

F_seq = fib_seq(10)
print("basic fib seq")
print(F_seq)


# element-at-a-time version
n=0 # global index variable
Fn1 = 0
Fn2 = 0
def fib_seq_next():
    global n
    global Fn1, Fn2

    if n == 0 or n == 1:
       n = n + 1
       return n-1  # pre-incremented index

    if n == 2:
       n = n+1 
       Fn2 = 1  # setup for next time
       Fn1 = 1  # setup for next time    
       return 1
    else:
      Fn = Fn1 + Fn2
      Fn2 = Fn1 # setup for next time
      Fn1 = Fn  # setup for next time
      n = n+1
      return(Fn)


print("element-at-a-time fib seq")
for k in range(10):
    print( fib_seq_next() )




