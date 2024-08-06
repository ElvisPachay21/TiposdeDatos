M1 =int(input("Ingrese su primera nota: "))
M2 = int(input("Ingrese su segunda nota: "))
M3 = int(input("Ingrese su tercera nota: "))
M4 = int(input("Ingrese su cuarta nota: "))

P = ( M1 + M2 + M3 + M4 ) / 4

if P >= 90  :
    print("Usted califica con A")
    
elif P >= 80:
    print("Usted califica con B")
elif P >= 70:
    print("Usted califica con C")
elif P >= 60:
    print("Usted califica con D")
elif P >= 50:
    print("Usted califica con E")
