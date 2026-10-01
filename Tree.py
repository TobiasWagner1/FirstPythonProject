baumhöhe = int(input("Wie hoch soll der Baum sein? "))
seitenabstand = baumhöhe - 1
anzahlblätter = 1

while seitenabstand > 0:
    print(" " * seitenabstand, "x" * anzahlblätter, " " * seitenabstand)
    seitenabstand -= 1
    anzahlblätter += 2

seitenabstand = baumhöhe - 1
print(" " * seitenabstand, "x", " " * seitenabstand)

