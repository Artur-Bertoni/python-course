
confirmedPurchase = True
purchaseData = 'Compra no valor de R$12.50 e entrega confirmada'

for send in range(3):
    if confirmedPurchase:
        print(purchaseData)
        print('Detalhes enviados para o seu email')
        break
else:
    print('Falha na compra')