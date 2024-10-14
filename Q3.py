import json

def analise_faturamento(arquivo_json):

    with open(arquivo_json, 'r') as f:
        dados = json.load(f)

    # Filtra os dias com faturamento e calcula a média
    faturamentos = [dado['valor'] for dado in dados if dado['valor'] > 0]
    media = sum(faturamentos) / len(faturamentos)

    # Encontra o menor e maior valor, e conta os dias acima da média
    menor_valor = min(faturamentos)
    maior_valor = max(faturamentos)
    dias_acima_media = sum(valor > media for valor in faturamentos)

    return menor_valor, maior_valor, dias_acima_media

arquivo = "C:\\desenv\\python\\estagio\\QUESTAO 3\\dados.json"
menor, maior, dias = analise_faturamento(arquivo)
print(f"Menor valor: R${menor:.2f}")
print(f"Maior valor: R${maior:.2f}")
print(f"Dias acima da média: {dias}")