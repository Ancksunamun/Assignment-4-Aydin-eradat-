
print("Calculation of Lcm between two number")

firstn=int(input("plz enter your first number:"))
secondn=int(input("plz enter your second number:"))


def lcm():
    higher = max(firstn, secondn)
    alt = higher
    while True:
        if higher % firstn == 0 and higher % secondn == 0:
            print("lcm between", str(firstn), "and", str(secondn), "is", str(higher))
            break
        else:
            higher=alt+ higher


lcm()

