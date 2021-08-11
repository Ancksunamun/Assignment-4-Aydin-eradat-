n=int (input("plz enter your number:"))


def factorial(a):
    b=1
    for i in range(1,a+1):
        b=i*b
    return b
c=1
while factorial(c) <= n:
    c+=1
    if factorial(c)==n:
        print("It is factorial number")
    elif factorial(c)> n:
        print("it is not a factorial number")
