peca1 = input().split()
peca2 = input().split()

cod1 = int(peca1[0])
num1 = int(peca1[1])
val1 = float(peca1[2])
cod2= int(peca2[0])
num2= int(peca2[1])
val2= float(peca2[2])

valor = (num1*val1)+(num2*val2)
print("VALOR A PAGAR: R$ %.2F" %valor)