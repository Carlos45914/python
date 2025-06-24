def rigth_justify(Palavra, TamanhoPalavra):
   espaco = " " * (70-TamanhoPalavra)
   return espaco + Palavra
#main
Palavra = str(input("digite uma palavra"))
TamanhoPalavra = len(Palavra)
justificado = rigth_justify(Palavra, TamanhoPalavra)

print(justificado)