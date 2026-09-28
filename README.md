Lista
```python
# declaracao da lista
lista = [10, 20, 30]
# acesso pelo indice (inicia em 0)
print(lista[0]) # imprime 10
```
```python
# lista com os precos dos produtos
precos = [10.5, 5.0, 3.2]
# soma todos os itens da lista
total = sum(precos)
# exibe o valor total da compra
print(f"Total: {total}")
```
```python
lista = [10, 20, 30]
# acesso pelo indice (inicia em 0)
print(lista[0]) # imprime 10
lista.remove(10) # Remove a primeira ocorrencia de um valor.
print(lista[0])
lista.append(40) # Adiciona um elemento ao final da lista.
print(lista[2])
lista.reverse() # Inverte a ordem dos elementos da lista.
print(lista[0])
lista.insert(1, 70) # Insere um elemento em uma posicao especifica.
print(lista[1])
```
```python
# lista com os precos dos produtos
precos = [10.5, 5.0, 3.2]
# soma todos os itens da lista
total = sum(precos)
# exibe o valor total da compra
print(f"Total: {total}")
precos.append(2)
total = sum(precos)
print(f"Total: {total}")
```
Tuplas
```python
# declaração da tupla (parenteses)
ponto = (10, 20 ,30)
# acesso pelo indice (inicia em 0)
print(ponto[0])    # imprime 10
# imprime a tupla inteira
print(ponto)       # (10, 20, 30)
# percorrendo a tupla
for valor in ponto:
    print(valor)
```
```python
# tupla com latitude e longitude (imutavel)
local = (12.45, -32.12)
# acesso pelos indices 0 e 1
print(f"Latitude: {local[0]}, Longitude: {local[1]}")
```
Conjuntos(sets)
```python
# declaracao do conjunto (chaves)
frutas = {"maca", "uva", "maca"}
# duplicatas sao eliminadas
print(frutas) # {'maca', 'uva'}
# teste de pertinencia (acesso)
print("uva" in frutas) # True
# percorrendo o conjunto
for f in frutas:
    print(f)
```

```python
# lista de entregas com nomes repetidos
entregas = ["Ana", "Joao", "Ana", "Pedro"]
# set() elimina as duplicatas
conjunto = set(entregas)
# imprime apenas os alunos unicos
print(conjunto)
```
```python
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
```
Operações Fundamentais
```python
# lista original de valores
lista = [10, 5, 20, 3, 42, 7]
# filtragem com list comprehension
maiores = [x for x in lista if x > 10]
print(maiores) # [20, 42]
# mesma filtragem com filter()
pares = list(filter(lambda x: x % 2 == 0, lista))
print(pares) # [10, 20, 42]
```
```python
# lista fora de ordem
lista = [10, 5, 20, 3]
# sort() ordena a propria lista
lista.sort()
print(lista) # [3, 5, 10, 20]
# ordem decrescente
lista.sort(reverse=True)
print(lista) # [20, 10, 5, 3]
# sorted() devolve uma nova lista
nova = sorted(lista)
```
```python
# dois conjuntos de valores
A = {1, 2, 3}
B = {3, 4, 5}
# uniao: tudo de A e de B
print(A | B) # {1, 2, 3, 4, 5}
# intersecao: o que ha nos dois
print(A & B) # {3}
# diferenca: so o que e de A
print(A - B) # {1, 2}
```
Operações Fundamentais

Manipulação de coleções: Adicionar, Remover, Atualizar, Iterar, Verificar pertencimento
```python
# arquivo: adicionar.py
def adicionar(estoque, produto):
    # evita duplicidade no estoque
    if produto not in estoque:
     estoque.append(produto) # insere
    return estoque
# teste rapido do modulo
if __name__ == "__main__":
    print(adicionar(["mouse"], "teclado"))
```
```python
# arquivo: remover.py
def remover(estoque, produto):
# so remove se o item existir
    if produto in estoque:
        estoque.remove(produto)
    else:
        print("Produto nao encontrado")
        return estoque
if __name__ == "__main__":
    print(remover(["mouse", "hd"], "hd"))
```
```python
# arquivo: atualizar.py
def atualizar(estoque, antigo, novo):
    # localiza o indice do produto
    if antigo in estoque:
        i = estoque.index(antigo)
        estoque[i] = novo # substitui
        return estoque
if __name__ == "__main__":
    print(atualizar(["mose"], "mose",
                    "mouse"))
```
```python
# arquivo: iterar.py
def iterar(estoque):
    # enumerate da indice e valor
    for i, produto in enumerate(estoque,
                                start=1):

        print(i, "-", produto)
    print("Total:", len(estoque))
if __name__ == "__main__":
    iterar(["mouse", "teclado"])
```
```python
# arquivo: pertencimento.py
def existe(estoque, produto):
    # o operador in devolve True/False
    return produto in estoque
if __name__ == "__main__":
    lista = ["mouse", "teclado"]
    if existe(lista, "mouse"):
        print("Ja cadastrado")
    else:
        print("Pode comprar")
```
```python
# arquivo: principal.py
from adicionar import adicionar
from remover import remover
from atualizar import atualizar
from iterar import iterar
from pertencimento import existe
estoque = ["mouse", "mose", "hd"]
adicionar(estoque, "teclado")
atualizar(estoque, "mose", "mouse2")
remover(estoque, "hd")
if existe(estoque, "teclado"):
    iterar(estoque) # relatorio final
```

4.5 Exercícios Guiados - 1
```python

```


