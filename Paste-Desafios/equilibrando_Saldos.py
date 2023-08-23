saldoAtual = float(input())
valorDeposito = float(input())
valorRetirada = float(input())

saldoAtual += valorDeposito
saldoAtual -= valorRetirada

print("Saldo atualizado na conta: {:.1f}".format(saldoAtual))

