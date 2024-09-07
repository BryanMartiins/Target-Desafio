import json


with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)

menor_valor = min(entrada ["valor"] for entrada in dados)
maior_valor = max(entrada ["valor"] for entrada in dados)
valor_media = sum(entrada ["valor"] for entrada in dados) / 21
valor = (entrada ["valor"] for entrada in dados)
dia = (entrada ["dia"] for entrada in dados)

print(f"O menor valor é: {menor_valor}")
print(f"O menor valor é: {maior_valor}")
print(f"O valor médio é: {valor_media:.2f}")

print("Dias com os valores acima da média")
for entrada in dados:
    if entrada["valor"] > valor_media:
        print(f"Dia {entrada['dia']}: {entrada['valor']:.2f}")

        

