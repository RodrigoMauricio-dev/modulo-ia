# Este programa calcula o preco total de uma compra

# Solicita informacoes sobre o produto ao usuario
nome_produto = input("Digite o nome do Produto: ")
preco_unitario = float(input("Digite o valor unitario do Produto: "))
quantidade = int(input("Digite a quantidade de Produtos: "))

# Calcula o preco total
preco_total = preco_unitario * quantidade

# Exibe o resultado
print(f"\nProduto: {nome_produto}")
print(f"Preço unitário: R$ {preco_unitario:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Total: R$ {preco_total:.2f}")