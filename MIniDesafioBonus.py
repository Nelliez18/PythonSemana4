# Módulo para cadastro, filtragem e análise estatística de preços de produtos.

def gerenciar_produtos():
    # Gerencia o cadastro de produtos, realiza filtragens e gera estatísticas.
    produtos = []
    
    print("=== Cadastro de Produtos (Digite 'sair' no nome para encerrar) ===")
    
    # 1. Cadastro dos produtos (Nome, Preço e Categoria)
    while True:
        nome = input("Nome do produto: ").strip()
        if nome.lower() == "sair":
            break
            
        if not nome:
            print("O nome do produto não pode ser vazio.")
            continue
            
        try:
            preco = float(input(f"Preço de '{nome}' (R$): "))
            if preco < 0:
                print("O preço não pode ser negativo.")
                continue
        except ValueError:
            print("Por favor, digite um valor numérico válido para o preço.")
            continue
            
        categoria = input(f"Categoria de '{nome}': ").strip().capitalize()
        if not categoria:
            categoria = "Sem Categoria"
            
        # Armazena cada produto como um dicionário dentro da lista principal
        produtos.append({
            "nome": nome,
            "preco": preco,
            "categoria": categoria
        })

    if not produtos:
        print("Nenhum produto foi cadastrado.")
        return

    # 1. Filtragem por preço informado
    print("\n--- Filtragem de Produtos ---")
    try:
        valor_corte = float(input("Digite um valor de preço para filtrar (R$): "))
        tipo_filtro = input("Deseja listar produtos 'acima' ou 'abaixo' deste valor? ").strip().lower()
        
        print(f"\nProdutos com valor {tipo_filtro} de R$ {valor_corte:.2f}:")
        encontrou_filtro = False
        
        for prod in produtos:
            if tipo_filtro == "acima" and prod["preco"] > valor_corte:
                print(f" • {prod['nome']} - R$ {prod['preco']:.2f} [{prod['categoria']}]")
                encontrou_filtro = True
            elif tipo_filtro == "abaixo" and prod["preco"] < valor_corte:
                print(f" • {prod['nome']} - R$ {prod['preco']:.2f} [{prod['categoria']}]")
                encontrou_filtro = True
                
        if not encontrou_filtro:
            print(" Nenhum produto atendeu ao critério de filtragem.")
    except ValueError:
        print("Valor de corte inválido. Pulando etapa de filtragem.")

    # 2. Ordenação (Crescente e Decrescente)
    # lambda especifica que a ordenação deve ser baseada na chave 'preco' de cada dicionário
    produtos_crescente = sorted(produtos, key=lambda x: x["preco"])
    produtos_decrescente = sorted(produtos, key=lambda x: x["preco"], reverse=True)

    # 2. Categorias únicas utilizando set()
    categorias_unicas = set(prod["categoria"] for prod in produtos)

    # 3. Tupla com estatísticas gerais
    lista_precos = [prod["preco"] for prod in produtos]
    menor_preco = min(lista_precos)
    maior_preco = max(lista_precos)
    media_precos = sum(lista_precos) / len(lista_precos)
    
    estatisticas = (menor_preco, maior_preco, media_precos)

    # 3. Relatório Final Formatado
    print("\n" + "="*50)
    print("                RELATÓRIO DE PRODUTOS             ")
    print("="*50)
    
    print("Produtos por ordem Crescente de Preço:")
    for prod in produtos_crescente:
        print(f" - {prod['nome']}: R$ {prod['preco']:.2f} ({prod['categoria']})")
        
    print("\nProdutos por ordem Decrescente de Preço:")
    for prod in produtos_decrescente:
        print(f" - {prod['nome']}: R$ {prod['preco']:.2f} ({prod['categoria']})")
        
    print(f"\nConjunto de Categorias Únicas (set): {categorias_unicas}")
    
    print("\nEstatísticas Gerais (Tupla):")
    print(f" • Menor Preço: R$ {estatisticas[0]:.2f}")
    print(f" • Maior Preço: R$ {estatisticas[1]:.2f}")
    print(f" • Média dos Preços: R$ {estatisticas[2]:.2f}")
    print("="*50)

if __name__ == "__main__":
    gerenciar_produtos()
