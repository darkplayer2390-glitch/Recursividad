from re import match


class Recursiviidad:


    #1. Factorial
    def factorial_iterativo(self, n:int) -> int:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

    def factorial_recursivo(self, n:int) -> int:
        if n <= 0:   #Caso base
            return 1
        else:   #Caso recursivo
            return n * self.factorial_recursivo(n - 1)


    #2. Fibonacci

    def fibonacci_iterativo(self, n:int) -> int:
        if n <= 1:
            return n
        f1, f2 = 1, 1
        while n > 2:
            nuevo = f1 + f2
            f1 = f2
            f2 = nuevo
            n -= 1
        return f2

    def fibonacci_recursivo(self, n:int) -> int:
        if n <= 1:
            return n
        else:
            return self.fibonacci_recursivo(n - 1) + self.fibonacci_recursivo(n - 2)


    #3. Problema 1
    def repetir(self):
        self.repetir()
    #*Se repite de manera infinita hasta que de error*


    #4. Problema 2
    def imprimir(self, n:int):
        print(f"{n}")
        self.imprimir(n - 1)


    #5. Problema 3
    def imprimir_decsendente(self, x:int):
        if x > 0:
            print(x, end=", ")
            self.imprimir_decsendente(x - 1)


    def imprimir_1_a_n(self, n: int):
        # Caso base: si n es mayor que 0, avanzamos
        if n > 0:
            # Primero llamamos a la función con un número menor
            self.imprimir_1_a_n(n - 1)
            # Al regresar de la recursividad, imprimimos el número
            print(n, end=" ")

    def invertir_cadena(self, cadena: str) -> str:
        if len(cadena) <= 1:
            return cadena
        else:
            return self.invertir_cadena(cadena[1:]) + cadena[0]

if __name__ == "__main__":
    re = Recursiviidad()
    opcion = -1

    while opcion != 0:
        print("\nOpciones:")
        print("1. Factorial")
        print("2. Fibonacci")
        print("3. Problema 1 (Repetir)")
        print("4. Problema 2 (Imprimir)")
        print("5. Problema 3 (Imprimir descendente)")
        print("6. Imprimir de 1 a n")
        print("7. Invertir cadena")
        print("0. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
            match opcion:
                case 1:
                    n = int(input("Ingrese un número para calcular su factorial: "))
                    print(f"Factorial iterativo de {n}: {re.factorial_iterativo(n)}")
                    print(f"Factorial recursivo de {n}: {re.factorial_recursivo(n)}")
                case 2:
                    n = int(input("Ingrese un número para calcular su Fibonacci: "))
                    print(f"Fibonacci iterativo de {n}: {re.fibonacci_iterativo(n)}")
                    print(f"Fibonacci recursivo de {n}: {re.fibonacci_recursivo(n)}")
                case 3:
                    re.repetir()
                case 4:
                    n = int(input("Ingrese un número para imprimir: "))
                    re.imprimir(n)
                case 5:
                    x = int(input("Ingrese un número para imprimir en orden descendente: "))
                    re.imprimir_decsendente(x)
                case 6:
                    n = int(input("Ingrese un número para imprimir de 1 a n: "))
                    re.imprimir_1_a_n(n)
                case 7:
                    cadena = input("Ingrese una cadena para invertir: ")
                    print(f"Cadena invertida: {re.invertir_cadena(cadena)}")
                case 0:
                    print("Saliendo del programa.")
                case _:
                    print("Opción no válida.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue
