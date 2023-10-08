a = int(input("tapez le 1er coefficent"))
b = int(input("tapez le 2eme coefficent"))
c = int(input("tapez le 3eme coefficent"))
delta = b ^ 2 -( 4 * a * c )
if delta < 0 : print("pas de solution")
if delta == 0 :
    X = b ^ 2 / (2 * a)
    print("la seule solution est", X)
if delta > 0 :
   x1 = (-b + delta ** 0.5) / (2*a)
   x2 = (-b - delta ** 0.5) / (2*a)
   print( "L'équation a deux solutions réelles : x1 =", x1, "et x2 =", x2)
    