valor = int(input("Digite o valor do produto: "))
porcentagem = int(input("Digite a porcentagem do desconto (sem o símbolo de porcentagem %)"))

#para desconto

desconto = valor * porcentagem / 100
valor_final = valor - desconto

print("o valor final será de: ", valor_final)

#para aumento

aumento = valor * porcentagem / 100
valor_final_2 = valor + porcentagem

print("o valor final será de: ", valor_final_2)