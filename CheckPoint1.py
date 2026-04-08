#Boas vindas e entrada de dados
print("Boas Vindas a Vinheria Agnello")
nome = input("Digite seu nome: ")
ende = input("Digite seu endereço: ")
ano = int(input("Digite seu ano de nascimento: "))

#Verificar idade (código continuará)
if 2026 - ano < 18:
    print("Menores de 18 anos não podem consumir bebidas alcoólicas")

#Escolha do vinho e precificação
print("Nossas opções de vinho hoje são:")
print("Vinho Branco  R$17,00")
print("Vinho Tinto   R$40,00")
print("Vinho Seco    R$35,00")
print("Vinho Rosé    R$50,00")
print("Vinho Verde   R$70,00")

vin = input("Digite o vinho que deseja comprar (Apenas o tipo): ")
qtd = int(input("Digite a quantidade de garrafas que você deseja: "))

if vin == 'Branco':
    val = 17
elif vin == 'Tinto':
    val = 40
elif vin == 'Seco':
    val = 35
elif vin == 'Rosé':
    val = 50
elif vin == 'Verde':
    val = 70

valf = val*qtd

#Frete caso compra menor que 150
if valf < 150:
    valf = valf + 50

if 2026 - ano >= 60:
    print("Você recebeu 5% de desconto")
    valf = valf * 0.95

#Finalização
print(f"Muito obrigado, {nome}")
print(f"Sua compra será entregue no endereço: {ende}")
print(f"Sua compra saiu por R${valf}")