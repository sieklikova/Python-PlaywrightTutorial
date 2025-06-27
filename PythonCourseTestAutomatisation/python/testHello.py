import math

koefa = input("zadej koeficient a:")
koefb = input("zadejte koeficient b:")
koefc = input("zadejte koeficient c:")
a = int(koefa)
b = int(koefb)
c = int(koefc)

det = b*b-4*a*c

def korenFunkce1(h1,h2,deter):
    koren = (-h2 + deter)/2*h1
    return (koren)
def korenFunkce2(k1,k2,kDeter):
    koren = (-k2 - kDeter)/2*k1
    return (koren)

print(f"kvadraticka rovnice: {koefa} x^2 + {koefb} x + {koefc}")
print(f"determinant: {det}")

#řešení rovnice př (1,2,1), dva kořeny(1,4,1), irac(2,1,2) no(0,3,2)
if det == 0 and a != 0:
   print("rovnice má jeden racionální kořen")
   sqDet = math.sqrt(det)
   koren = korenFunkce1(a,b,sqDet)
   print(f"Řešením rovnice je racionální kořen: {koren}")

elif det > 0 and a != 0:
   print("Rovnice má dva racionální kořeny")
   sqDet1 = math.sqrt(det)
   koren1 = korenFunkce1(a,b,sqDet1)
   koren2 = korenFunkce2(a,b,sqDet1)
   print(f"kořen1: {koren1} a kořen2: {koren2}")

elif det < 0 and a != 0:
   print("Rovnice má dva iracionální kořeny")
   absDet = math.fabs(det)
   absKoren1 = korenFunkce1(a,b,absDet)
   absKoren2 = korenFunkce2(a,b,absDet)

   print(f"kořen1: {absKoren1}i a kořen2: {absKoren2}i")

# jmenovatel je 0   
else:
   print("rovnice nemá řešení")
