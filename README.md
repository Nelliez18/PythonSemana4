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
lista.remove(10)
print(lista[0])
lista.append(40)
print(lista[2])
lista.reverse()
print(lista[0])
```
Tuplas
```python
# Tuplas
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
