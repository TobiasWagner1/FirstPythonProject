
rautenhöhe = int(input("Wie hoch soll die Raute sein?"))
anzahlsterne = 1
anzahlleerzeichen = rautenhöhe - 1

while anzahlleerzeichen > 0:
    print(" " * anzahlleerzeichen + "x" * anzahlsterne + " " * anzahlleerzeichen)
    anzahlsterne += 2
    anzahlleerzeichen -= 1

print("x" * anzahlsterne)

anzahlsterne = 2*rautenhöhe -3
anzahlleerzeichen = 1

while anzahlsterne > 0:
    print (" " * anzahlleerzeichen + "x" * anzahlsterne)
    anzahlsterne -= 2
    anzahlleerzeichen += 1




