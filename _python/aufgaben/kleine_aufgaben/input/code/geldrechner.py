zwei_eu = int(input("Wie viele 2€ Stücke hast du: "))
geld = zwei_eu * 2
ein_eu = int(input("Wie viele 1€ Stücke hast du: "))
geld = geld + ein_eu * 1
fuenfzig_ct = int(input("Wie viele 50ct Stücke hast du: "))
geld = geld + fuenfzig_ct * 0.5
zwanzig_ct = int(input("Wie viele 20ct Stücke hast du: "))
geld = geld + zwanzig_ct * 0.2
zehn_ct = int(input("Wie viele 10ct Stücke hast du: "))
geld = geld + zehn_ct * 0.1
fuenf_ct = int(input("Wie viele 5ct Stücke hast du: "))
geld = geld + fuenf_ct * 0.05
zwei_ct = int(input("Wie viele 2ct Stücke hast du: "))
geld = geld + zwei_ct * 0.02
ein_ct = int(input("Wie viele 1ct Stücke hast du: "))
geld = geld + ein_ct * 0.01

print("Du hast " + str(geld) + " €")
