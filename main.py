class CalculadoraMCD:
    def calcular_mcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def calcular_mcm(self, a, b):
        return (a * b) // self.calcular_mcd(a, b)


# Crear una instancia de la clase CalculadoraMCD
calculadora = CalculadoraMCD()

# Solicitar al usuario que ingrese los números
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Calcular el MCD y el MCM
mcd = calculadora.calcular_mcd(num1, num2)
mcm = calculadora.calcular_mcm(num1, num2)

# Mostrar el MCD y el MCM
print("El MCD de", num1, "y", num2, "es:", mcd)
print("El MCM de", num1, "y", num2, "es:", mcm)