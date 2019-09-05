salario = (float(input("Digite o salario: ")))
aumento = (float(input("Digite a porcentagem do aumento: ")))

valorAumento = ((salario+aumento)/100)
novoSalario = (salario+valorAumento)

print("O valor do aumento é: ",(valorAumento))
print("O novo salario é: " ,(novoSalario))
