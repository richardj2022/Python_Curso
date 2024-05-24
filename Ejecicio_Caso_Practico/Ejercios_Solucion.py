def AgregarCirculo():
    radio = float(input("Ingresar el radio de la Circunferencia: "))

def AgregarTriangulo():
    lado1 = float(input("Ingresar lado # 1: "))
    lado2 = float(input("Ingresar lado # 2: "))
    lado3 = float(input("Ingresar lado # 3: "))
    
class FiguraGeometrica():
    "Realizar calculo"    

def CalculadoraFiguras():
    "Realizar calculo"   

def Salir():
    "Salir"
  
while True:
    print("***Que desea realizar***")
    print("1. Agregar Círculo.")   
    print("2. Agregar Triángulo.") 
    print("3. Calcular Totales.") 
    print("4. Salir.") 
    
    opc = input("Ingrese su opción: ")
    
    if opc=="1":
        AgregarCirculo()
    elif opc=="2":
        AgregarTriangulo()
    elif opc=="3":
        pass
    elif opc=="4":
        pass
    else:
        print("Opción invalida. Intente nuevamente.")
    