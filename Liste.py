noten = [1,2,3,4,5]

def durchschnitt (x):
    return (sum(x)/len(x))

def durchschnitt2 (y):
    Summe = 0
    Index = 0

    for i in range(0,len(y)):
        Summe = Summe + y[Index]
        Index = Index + 1

    return Summe / len(y)

print(durchschnitt(noten))
print(durchschnitt2(noten))

