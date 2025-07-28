# Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço
# normal deetiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir
# para ler qual acondição de pagamento escolhida e efetuar o cálculo adequado.
# Código Condição de pagamento
# 1 À vista em dinheiro ou cheque, recebe 10% de desconto
# 2 À vista no cartão de crédito, recebe 15% de desconto
# 3 Em duas vezes, preço normal de etiqueta sem juros
# 4 Em duas vezes, preço normal de etiqueta mais juros de 10%

preco = float(input("Digite o preço do produto: "))
codigo = int(input("Forma de pagamento (1-4): "))

if codigo == 1:
    print("Valor a pagar: R$", preco * 0.90)
elif codigo == 2:
    print("Valor a pagar: R$", preco * 0.85)
elif codigo == 3:
    print("Valor a pagar: R$", preco)
elif codigo == 4:
    print("Valor a pagar: R$ {:.2f}".format(preco * 1.10)) 
else:
    print("Código inválido.")
