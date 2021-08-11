def gcd(a,b):

    if b == 0:
        return  a

    else:
        return gcd(b,a%b)



print("calculation of gcd between two numbers")
n1=int(input("Plz enter your first number:"))
n2= int(input("Plz enter your second number:"))

print (gcd(n1,n2))





