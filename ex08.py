horasTrabalhadas = float(input("Digite o número de horas trabalhadas: "))
salarioMinimo = float(input("Digite o valor do salário mínimo: "))
#calculo do valor da hora trabalhada
valorHoraTrabalhada = (salarioMinimo / 0.5)
#calculo do salario bruto
salarioBruto = (horasTrabalhadas * valorHoraTrabalhada)
#calculo do imposto
imposto = (salarioBruto*3)
imposto = (imposto/100)
#calculo salario a receber
salarioReceber = (salarioBruto - imposto)
print ("O seu salário a receber é: ", salarioReceber)
