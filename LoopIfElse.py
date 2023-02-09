
compraConfirmada = True
dadosCompra = 'compra no valor x e entrega confirmada'

for enviar in range(3):
    if compraConfirmada:
        print(dadosCompra)
        break
else:
    print('Falhou')   