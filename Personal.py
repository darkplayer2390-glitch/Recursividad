class Recursividad_2:

    def imprimir_descendente(self, n: int):
        """Imprime los números de n hasta 0 en orden descendente"""
        if n < 0:
            return
        print(n, end=" ")
        self.imprimir_descendente(n - 1)

    def imprimir_1_a_n(self, n: int):
        """Imprime los números de 1 a n en orden ascendente"""
        if n > 0:
            self.imprimir_1_a_n(n - 1)
            print(n, end=" ")

    def invertir_cadena(self, cadena: str) -> str:
        """Invierte una cadena de texto utilizando recursividad"""
        if len(cadena) <= 1:
            return cadena
        return cadena[-1] + self.invertir_cadena(cadena[:-1])

    def sumar_naturales(self, n: int) -> int:
        """Suma de forma recursiva los primeros n números naturales"""
        # Caso base: si n es 0, la suma es 0
        if n == 0:
            return 0
        # Paso recursivo: n + la suma de los anteriores
        return n + self.sumar_naturales(n - 1)

if __name__ == "__main__":
    rec = Recursividad_2()
    opcion = -1

    while opcion != 0:
        print("\nOpciones:")
        print("1. Imprimir descendente")
        print("2. Imprimir de 1 a n")
        print("3. Invertir cadena")
        print("4. Sumar naturales")
        print("0. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
            match opcion:
                case 1:
                    n = int(input("Ingrese un número para imprimir en orden descendente: "))
                    rec.imprimir_descendente(n)
                case 2:
                    n = int(input("Ingrese un número para imprimir de 1 a n: "))
                    rec.imprimir_1_a_n(n)
                case 3:
                    cadena = input("Ingrese una cadena para invertir: ")
                    resultado = rec.invertir_cadena(cadena)
                    print(f"Cadena invertida: {resultado}")
                case 4:
                    n = int(input("Ingrese un número para sumar los primeros n naturales: "))
                    resultado = rec.sumar_naturales(n)
                    print(f"Suma de los primeros {n} naturales: {resultado}")
                case 0:
                    print("Saliendo del programa.")
                case _:
                    print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")