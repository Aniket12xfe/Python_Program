import sys

print("Enter the number to fill the tank.")

lit = int(input())

lt = (lit*1.00)

if lit < 1:
    print("{} is an invalid input".format(lit))
    sys.exit()

print("Enter the distance covered.")
dist = int(input())

dis = (dist*1.00)

if dist < 0:
    print("{} is an invalid input".format(dist))
    sys.exit()

hundred = ((lt/dis)*100)

print("Liters/100km")
hundred_rounded = round(hundred, 2)
print(hundred_rounded)
miles = (dis*0.6214)
gallons = (lt*0.2642)

mg = (miles/gallons)

print("Miles/gallons")
mg_rounded = round(mg, 2)
print(mg_rounded)