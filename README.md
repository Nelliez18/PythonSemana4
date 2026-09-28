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


