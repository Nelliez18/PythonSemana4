"""Módulo para gerenciamento, filtragem e ordenação de uma lista de nomes."""

def gerenciar_nomes():
    """Lê uma lista de nomes, remove duplicatas, ordena e exibe um relatório."""
    nomes_originais = []
    
    print("=== Cadastro de Nomes (Digite 'sair' para encerrar) ===")
    
    # 1. Criar lista de nomes usando input() e append()
    while True:
        entrada = input("Digite um nome: ").strip()
        
        if entrada.lower() == 'sair':
            break
            
        if entrada:
            nomes_originais.append(entrada)

    if not nomes_originais:
        print("Nenhum nome foi digitado.")
        return

    # 2. Remover duplicatas usando set()
    nomes_unicos_set = set(nomes_originais)
    
    # 3. Ordenar alfabeticamente usando sorted()
    lista_ordenada = sorted(list(nomes_unicos_set))
    
    # 4. Criar tupla com o primeiro [0] e último [-1] nome da lista ordenada
    tupla_extremos = (lista_ordenada[0], lista_ordenada[-1])
    
    # 5. Exibir relatório final com f-strings
    print("\n" + "="*40)
    print("             RELATÓRIO FINAL            ")
    print("="*40)
    print(f"Total de nomes digitados: {len(nomes_originais)}")
    print(f"Quantidade de nomes únicos: {len(lista_ordenada)}")
    print(f"Lista ordenada de A a Z: {lista_ordenada}")
    print(f"Tupla (Primeiro, Último): {tupla_extremos}")
    print("="*40)

if __name__ == "__main__":
    gerenciar_nomes()



# VERSÃO INTEGRAL EM PORTUGOL COMENTADA
#
# programa {
#     funcao inicio() {
#         cadeia nomes_originais
#         cadeia nomes_unicos
#         cadeia entrada = ""
#         cadeia aux
#         
#         inteiro total_digitados = 0
#         inteiro total_unicos = 0
#         inteiro i, j
#         logico duplicado
#
#         enquanto (entrada != "sair" e total_digitados < 100) {
#             escreva("Digite um nome: ")
#             leia(entrada)
#             se (entrada != "sair" e entrada != "") {
#                 nomes_originais[total_digitados] = entrada
#                 total_digitados = total_digitados + 1
#             }
#         }
#
#         se (total_digitados == 0) {
#             escreva("Nenhum nome foi digitado.\n")
#             retorne
#         }
#
#         // Remoção de duplicatas
#         para (i = 0; i < total_digitados; i++) {
#             duplicado = falso
#             para (j = 0; j < total_unicos; j++) {
#                 se (nomes_originais[i] == nomes_unicos[j]) {
#                     duplicado = verdadeiro
#                     pare
#                 }
#             }
#             se (nao duplicado) {
#                 nomes_unicos[total_unicos] = nomes_originais[i]
#                 total_unicos = total_unicos + 1
#             }
#         }
#
#         // Ordenação por Método da Bolha
#         para (i = 0; i < total_unicos - 1; i++) {
#             para (j = 0; j < total_unicos - i - 1; j++) {
#                 se (nomes_unicos[j] > nomes_unicos[j + 1]) {
#                     aux = nomes_unicos[j]
#                     nomes_unicos[j] = nomes_unicos[j + 1]
#                     nomes_unicos[j + 1] = aux
#                 }
#             }
#         }
#
#         // Exibição direta dos dados do relatório
#         escreva("Total de nomes digitados: ", total_digitados, "\n")
#         escreva("Quantidade de nomes únicos: ", total_unicos, "\n")
#         
#         escreva("Lista ordenada de A a Z: ")
#         para (i = 0; i < total_unicos; i++) {
#             escreva(nomes_unicos[i], " ")
#         }
#         
#         escreva("\nTupla (Primeiro, Último): (", nomes_unicos, ", ", nomes_unicos[total_unicos - 1], ")\n")
#     }
# }
