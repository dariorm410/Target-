import json

with open('C:\\Users\\dario\\OneDrive\\Área de Trabalho\\Target Sistemas\\q3-Faturamento via JSON\\dados.json', 'r') as file:
    dados = json.load(file)

# Calculando o menor valor de faturamento diário
menor_valor = min([dia['valor'] for dia in dados])

# Calculando o maior valor de faturamento diário
maior_valor = max([dia['valor'] for dia in dados])

# Calculando a média mensal de faturamento diário (ignorando dias sem faturamento)
dias_com_faturamento = [dia['valor'] for dia in dados if dia['valor'] > 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

# Calculando o número de dias no mês em que o valor de faturamento diário foi superior à média mensal
dias_acima_da_media = len([dia for dia in dados if dia['valor'] > media_mensal])

print(f"Menor valor de faturamento diário: R$ {menor_valor:.2f}")
print(f"Maior valor de faturamento diário: R$ {maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")
