def adicao(numro, numro2):
  return numero + numero2

def subritacao(numero, numero2):
  return numero - numero2

def multiplicacao(numero, numero2):
    return numero * numero2

def divisao(numero, numero2):
    return numero / numero2
# main
numero = int(input("digiteo primeiro numero "))
numero2 = int(input("digite o segundo numero"))

resultadoAdicao = adicao(numero, numero2)
resultadoSubritacao = subritacao(numero, numero2)
resultadoMultiplicacao = multiplicacao(numero, numero2)
resultadoDivisao = divisao(numero, numero2)

print("Adicao, resultadoAdicao")
print("Subritacao, resultadoSubritacao")
print("Multiplicacao, resultadoMultiplicacao")
print("Divisao, resultadoDivisao")