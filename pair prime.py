s=int(input('Enter starting value:'))
e=int(input('Enter ending value:'))
def prime(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return x
for i in range(s,e-2):
    if(prime(i) and prime(i+2)):
        print(prime(i),"and",prime(i+2),"is pair prime.")
    else:
        continue
