class Calculadora:
    
    def sumar(self, numeros):
       return sum(numeros)
        
    def restar(self, numeros):
        if not numeros:
            return 0
        else:
            primer_numero = numeros[0]
            for numero in numeros:
                primer_numero -= numero
        return primer_numero
    
    def multiplicaciones(self, numeros):
        resultado = 1
        for numero in numeros:
            resultado *= numero
        return resultado
    
    def division(self,numeros):
        if not numeros:
            print("No hay numeros para dividir")
        else:
            primer_numero = numeros[0]
            for numero in numeros:
                if numero == 0:
                    return "No se puede dividir entre 0"
                else:
                    primer_numero /= numero
        return primer_numero
    
def mostrar_menu():
    print("Seleccione una de las opciones:")
    print("1. Sumar n numeros")
    print("2. Restar n numeros")
    print("3. Multiplicar n numeros")
    print("4. Dividir n numeros")
    print("5. Salir")              
    
    
def obtener_numeros():
        numeros = []
        while True:
            entrada = input("Ingrese el numero (en caso de salir del menu 'fin') -->")
            if entrada.lower() == 'fin':
                break
            try:
                numero = float(entrada)
                numeros.append(numero)
            except ValueError:
                print("No existe esa opcion")
        return numeros
    
def main():
        calculadora = Calculadora()
        
        while True:
            mostrar_menu()
            opcion = input("Ingrese el numero de la operacion que desea realizar --> ")
            if opcion == '5':
                print("Gracias por usar el programa :D")
                break
            else:
                numeros = obtener_numeros()
                if not numeros:
                    print("No hay numeros para realizar la operacion")
                    continue
                if opcion == '1':
                    resultado = calculadora.sumar(numeros)
                elif opcion == '2':
                    resultado = calculadora.restar(numeros)
                elif opcion == '3':
                    resultado == calculadora.multiplicaciones(numeros)
                elif opcion == '4':
                    resultado = calculadora.dividir(numeros)
                else:
                    print("No existe esa opcion")
                    continue
                
            print(f"El resultado es --> {resultado}")

if __name__ == '__main__':
    main()
            
            