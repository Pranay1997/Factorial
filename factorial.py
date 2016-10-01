def fact(n):
    rtr=1 if n<=1 else n*fact(n-1)
    return rtr

n = int(input("Enter n: "))
print fact(n)
