frutas = {"maca", "uva", "maca"}
sucos = {"maca", "laranja", "abacaxi"}
# duplicatas sao eliminadas
print(frutas) # {'maca', 'uva'}
# teste de pertinencia (acesso)
print("uva" in frutas) # True
# percorrendo o conjunto
for f in frutas:
    print(f)
frutas.add("pera")     # Adiciona um elemento ao conjunto.
print(frutas)
frutas.remove("uva")   # Remove o elemento; erro se nao existir.
print(frutas)
frutas.discard("kiwi") # Remove o elemento sem gerar erro.
print(frutas)
frutas = frutas.union(sucos) # Une dois conjuntos (todos os itens).
print(frutas)
frutas = frutas.intersection(sucos) # Retorna os itens comuns aos dois conjuntos.
print(frutas)

# Reset 
frutas = {"maca", "uva", "maca"}
sucos = {"maca", "laranja", "abacaxi"}
frutas = frutas.difference(sucos) # Retorna os itens que estao so em Frutas.
print(frutas)
frutas = len(frutas) # Retorna a quantidade de itens unicos.
print(frutas)