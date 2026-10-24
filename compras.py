
print("--- Sistema de Compras Iniciado ---")

valores_brutos = []
valores_finais = []
descontos = []


while True:
    Valor_de_Compra = float(input("Digite o valor da compra(ou 0 para sair): "))

    if Valor_de_Compra < 0:
        print("Aviso: Você digitou errado. Tente Novamente!")
        continue

    if Valor_de_Compra == 0:
        print("Encerrando o sistema de compras. Até logo!")
        break

    Idade_do_Cliente = int(input("Digite a idade do cliente: "))

    if Idade_do_Cliente < 0:
        print("Aviso: Você digitou errado. Tente Novamente!")
        continue

    if Idade_do_Cliente >= 65:
        Valor_com_Desconto_Idade = Valor_de_Compra - (Valor_de_Compra * 0.20)
    else:
        Valor_com_Desconto_Idade = Valor_de_Compra

    if Valor_com_Desconto_Idade > 100:
        valor_total_de_descontos = Valor_com_Desconto_Idade - (Valor_com_Desconto_Idade * 0.10)

        if Idade_do_Cliente >= 65:
            print(f"O valor total da compra com todos os descontos é: R$ {valor_total_de_descontos:.2f}")       
        else:
            print(f"O valor total com somente o desconto de valor é: R$ {valor_total_de_descontos:.2f}")
    else:
        valor_total_de_descontos = Valor_com_Desconto_Idade
        if Idade_do_Cliente >= 65:
            print(f"O valor total com somente o desconto de idade é: R$ {valor_total_de_descontos:.2f}")
        else:
            print(f"Nenhum desconto aplicado. O valor total da compra é: R$ {valor_total_de_descontos:.2f}")

    desconto_da_rodada = Valor_de_Compra - valor_total_de_descontos

    valores_brutos.append(Valor_de_Compra)
    valores_finais.append(valor_total_de_descontos)
    descontos.append(desconto_da_rodada)

    print(f"Compra registrada! Valor a pagar: R$ {valor_total_de_descontos: .2f}\n")

print("\n---- Resumo do Dia ----")
print(f"Quantidade de compras registradas: {len(valores_brutos)}")
print(f"Total bruto: R$ {sum(valores_brutos):.2f}")
print(f"Total de descontos concedidos: R$ {sum(descontos):.2f}")
print(f"Total final (compras com desconto): R$ {sum(valores_finais):.2f}")
