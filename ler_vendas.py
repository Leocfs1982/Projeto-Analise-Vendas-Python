import csv
from pathlib import Path

def formatar_reais(valor):
    valor_formatado = f"{valor:,.2f}"
    valor_formatado = valor_formatado.replace(",", "X")
    valor_formatado = valor_formatado.replace(".", ",")
    valor_formatado = valor_formatado.replace("X", ".")
    return f"R$ {valor_formatado}"

faturamento_total = 0
quantidade_total = 0
lista_faturamentos = []
maior_faturamento = 0
produto_maior_faturamento = ""
menor_faturamento = None
produto_menor_faturamento = ""
total_produtos = 0

print("=" * 45)
print("       RELATORIO DE ANALISE DE VENDAS")
print("              CONTROLE COMERCIAL")
print("=" * 45)
print()

print("1. FATURAMENTO POR PRODUTO")
print("-" * 45)

caminho_csv = Path(__file__).parent / "vendas.csv"

with open(caminho_csv, "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)

    cabecalho = next(leitor)

    for linha in leitor:
        if not linha:
            continue

        if len(linha) < 3:
            print("Linha incompleta no arquivo CSV:", linha)
            continue

        produto = linha[0]
        try:
            quantidade = int(linha[1])
            preco = float(linha[2])
        except ValueError:
            print(f"Dados inválidos para o produto: {linha[0]}")
            continue
        if quantidade <= 0 or preco <= 0:
            print(f"Quantidade inválida ou preço negativo para o produto: {produto}")
            continue
        total_produtos += 1
        faturamento = quantidade * preco
        lista_faturamentos.append((produto, faturamento))
        faturamento_total += faturamento
        quantidade_total += quantidade
        
        if faturamento > maior_faturamento:
            maior_faturamento = faturamento
            produto_maior_faturamento = produto
        if menor_faturamento is None or faturamento < menor_faturamento:
            menor_faturamento = faturamento
            produto_menor_faturamento = produto
        
        print(f"{produto}: {formatar_reais(faturamento)}")
        
lista_faturamentos.sort(key=lambda item: item[1], reverse=True)
print("-" * 30)
print("2. RANKING DE PRODUTOS POR FATURAMENTO")
for produto, faturamento in lista_faturamentos:
    print(f"{produto}: {formatar_reais(faturamento)}")
print("-" * 30)

print("3. PARTICIPACAO NO FATURAMENTO TOTAL")

if faturamento_total > 0:
    for produto, faturamento in lista_faturamentos:
        percentual = (faturamento / faturamento_total) * 100
        print(f"{produto}: {percentual:.2f}% do faturamento total")
else:
    print("Não há faturamento válido para calcular os percentuais.")

print("=" * 30)
print("4. RESUMO GERAL DAS VENDAS")
print(f"Faturamento total: {formatar_reais(faturamento_total)}")

if total_produtos > 0:
    print(f"Produto com maior faturamento: {produto_maior_faturamento}")
    print(f"Valor: {formatar_reais(maior_faturamento)}")
    print(f"Produto com menor faturamento: {produto_menor_faturamento}")
    print(f"Valor: {formatar_reais(menor_faturamento)}")
else:
    print("Não há produtos válidos para identificar maior e menor faturamento.")

print(f"Quantidade total vendida: {quantidade_total} unidades")

if total_produtos > 0:
    media_faturamento = faturamento_total / total_produtos
    print(f"Faturamento médio por produto: {formatar_reais(media_faturamento)}")
else:
    print("Não há produtos para calcular a média.")