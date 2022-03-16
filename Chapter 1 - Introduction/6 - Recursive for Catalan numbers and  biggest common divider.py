#Catalan numbers using recursion
def Cn(n):
    if n == 0:
        return 1
    else:
        return ((4*n - 2)/(n+1))*Cn(n-1)
print(Cn(100))

#Biggest common divider using recursion
def g(m,n):
    if n == 0:
        return m
    else:
        return g(n,m%n)

print(g(108,192))
