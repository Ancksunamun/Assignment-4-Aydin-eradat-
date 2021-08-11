def raser_odd(a):
    for i in range(1,a+1):

        if i%2==0:
            print("* ",end="")
        if i%2==1:
            print("# ",end="")


def raser_even(b):
    for i in range(1,b+1):

        if i%2==1:
            print("* ",end="")
        if i%2==0:
            print("# ",end="")



print("m*n raser graphic print")
m=int(input("plz enter m:"))
n=int(input("plz enter n:"))

while n>0:
    if n%2==1:
        raser_odd(m)
        print("\n")
        n-=1

    if n%2==0:
        raser_even(m)
        print("\n")
        n-=1
