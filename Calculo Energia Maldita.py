carisma = float(input("Ingrese su carisma: "))

competencia = float(input("Ingrese su competencia: "))

nivel = float(input("Ingrese su nivel: "))

#calculo con inmensa energia maldita y energia maldita desbordante
#calculo solo con inmesa energia maldita == (nivel.2+cha.2+comp).2
#calculo sin nada == (nivel.2+cha.).2
em=((nivel+nivel/2)*2+carisma*2+competencia*2)*2




print (f"Su energia maldita es: {em}")