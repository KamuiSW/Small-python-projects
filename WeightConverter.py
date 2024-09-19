weight = input("whats your weight: ")
KorL = input("(K)kg or (L)bs: ")

if KorL == 'K':
    print("your weight in lbs, " + str(int(float(weight) * 2.20462262)))
elif KorL == 'L':
    print("your weight in kg, " + str(int(float(weight) * 0.45359237)))
else:
    print("sorry, please choose between K and L")
    