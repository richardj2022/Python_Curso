# Tipos de datos
# print("Python tiene los tipos de datos interpretados")
# FUNCIONES.
# COMANDOS.

# VARIABLE
# Dato numérico
precio = 45
precio
print(type(precio)) 
# Dato Float tipo de dato numérico con decimal
descuento = 15.4
print(descuento)
print(type(descuento))
# Si utilizas mayúsculas con el mismo nombre son dos variables diferentes.
# Precio = 20 es diferente de precio = 45
# Tipo de dato texto string
nombre = "Iphone"
print(nombre)
print(type(nombre))
# Tipo de dato cadena de texto  
iva = "6"
print(iva)
print(type(iva))
# Tipo de datos Booleanos:  Un dato Booleano que solo puede tener dos posibles valores TRUE O FALSE
activo = True
print(activo)
print(type(activo))
# Tipo de dato None
contenido = None
print(contenido)
print(type(contenido))

# Lo que se puede hacer con estos datos 
# cambiar el tipo de variable
#entero
iva = int(iva)
# de tipo float
#iva = float(iva)
#tipo texto
#iva = str(iva)
# ejemplo de calculo
precio_final = 300
precio_final_con_iva = precio_final * iva / 100
print(precio_final_con_iva)
texto = 'y yo le dije:"hola"'
print(texto)
# tipo de datos string o cadenas de texto
nombre = "Javier"
apellido = "Gomez"
nombre_completo = nombre +" "+ apellido
print(nombre_completo)
