def Rautebauen(zahl):
    anzahlsterne = 1
    anzahlleerzeichen = zahl - 1

    while anzahlleerzeichen > 0:
        print(" " * anzahlleerzeichen + "x" * anzahlsterne + " " * anzahlleerzeichen)
        anzahlsterne += 2
        anzahlleerzeichen -= 1

    print("x" * anzahlsterne)

    anzahlsterne = 2 * zahl - 3
    anzahlleerzeichen = 1

    while anzahlsterne > 0:
        print(" " * anzahlleerzeichen + "x" * anzahlsterne)
        anzahlsterne -= 2
        anzahlleerzeichen += 1


Rautebauen(4)

