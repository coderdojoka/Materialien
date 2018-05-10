t = input("Gib eine Jahreszahl ein:")
tipp = int(t)
x = tipp % 400
if x == 0:
    print("Es ist ein Schaltjahr")
else:
    x = tipp % 4
    if x != 0:
        print("Es ist kein Schaltjahr")
    else:
        x = tipp % 100
        if x == 0:
            print("Es ist kein Schaltjahr")
        else:
            print("Es ist ein Schaltjahr")

'''
Bedingungen:

Durch 400:Ist eines
Ansonsten:
    Nicht durch 4:Ist keines
    Ansonsten:
        Durch 100:Ist keines
        Ansonsten:Ist eines

'''
