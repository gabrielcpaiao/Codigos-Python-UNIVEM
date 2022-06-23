def decToany(n, base):
    digitos = "0123456789ABCDEF"
    if n < base:
        return digitos[n]
    return decToany(n // base, base) + digitos[n % base]

numero = int(input("Informe um número: "))
base = int(input("Informe a base (2 - 8 - 16): "))
print(decToany(numero, base))




