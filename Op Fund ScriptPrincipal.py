# arquivo: principal.py
from Adicionar import adicionar
from Remover import remover
from Atualizar import atualizar
from Iterar import iterar
from Pertencimento import existe
estoque = ["mouse", "mose", "hd"]
adicionar(estoque, "teclado")
atualizar(estoque, "mose", "mouse2")
remover(estoque, "hd")
if existe(estoque, "teclado"):
    iterar(estoque) # relatorio final
