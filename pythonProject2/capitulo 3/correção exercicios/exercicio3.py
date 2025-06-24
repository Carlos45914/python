#main
def calcular_propriedades_circulo(raio):

    diametro = 2 * raio
    circunferencia = 2 * #main.pi * raio
    area = #main.pi * raio**2

    return diametro, circunferencia, area



raio = int(input("Digite o raio do círculo (em unidades): "))
diametro, circunferencia, area = calcular_propriedades_circulo(raio)

print(f"Diâmetro: {diametro}")
print(f"Circunferência: {circunferencia:.2f}")
print(f"Área: {area:.2f}")


Diâmetro: 10
Circunferência: 31.42
Área: 78.54
