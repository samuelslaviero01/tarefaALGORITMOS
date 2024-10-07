def maior(x):
    return x >= 18


idades = [18]


for i in range(2):
    idade = int(input("Digite a idade: "))
    idades.append(idade)
    if maior(idade):
        print("Ele é de maior")
    else:
        print("Ele é de menor")
