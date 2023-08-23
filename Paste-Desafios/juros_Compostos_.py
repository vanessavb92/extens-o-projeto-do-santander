def calcular_valor_final(valor_inicial, taxa_juros, periodo):
    valor_final = valor_inicial * (1 + taxa_juros) ** periodo
    valor_final = round(valor_final, 2)
    return valor_final

valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

valor_final = calcular_valor_final(valor_inicial, taxa_juros, periodo)

print("Valor final do investimento: R$ {:.2f}".format(valor_final))
