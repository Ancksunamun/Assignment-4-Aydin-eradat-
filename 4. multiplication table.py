def row(a):
    for i in range(1,n+1):
        print(i*a,end=" ")

print("Mulriplication table in size of n * m")
n=int(input("Plz enter n:"))
m=int(input("Plz enter m:"))

for j in range(1,m+1):
    row(j)
    print("\n")




