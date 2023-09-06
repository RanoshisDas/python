#Write a program to print numbers from lower limit to uper limit
l=int(input('Enter lower limit'))
u=int(input('Enter uper limit'))
for i in range(l,u+1): #using u+1 because it will check condition upto u-1 times
    print(i,end=' ')