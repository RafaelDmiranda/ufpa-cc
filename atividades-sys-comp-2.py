#!/usr/bin/env python
# coding: utf-8

######Atividade1#########
quant_levels = int(input("Entre o número de níveis da quantização: "))

# Calcular o número de bits para representar os níveis de quantização
bits = 1
while 2 ** bits < quant_levels:
    bits += 1

print(f"Número de bits requeridos: {bits}")

# Gerar combinações de bits
combinations = []
for i in range(2 ** bits):
    binary = bin(i)[2:].zfill(bits)
    combinations.append(binary)

print("Todas combinações possíveis de bits:")
for combination in combinations:
    print(combination)

##########Atividade2#############

binary = input("Insira número binário: ")
decimal = 0

for digit in binary:
    decimal = decimal * 2 + int(digit)

print("Decimal equivalente:", decimal)

########Atividade3###############

decimal = int(input("Insira um número decimal: "))
binary = ""

while decimal > 0:
    binary = str(decimal % 2) + binary
    decimal //= 2

print("Binário equivalente:", binary)

################Atividade4##############

def float_bin(number, places=3):
    whole, dec = str(number).split(".")
    whole = int(whole)
    dec = int(dec)
    res = bin(whole).lstrip("0b") + "."
    for x in range(places):
        whole, dec = str((decimal_converter(dec)) * 2).split(".")
        dec = int(dec)
        res += whole
    return res

def decimal_converter(num):
    while num > 1:
        num /= 10
    return num

n = input("Insira o número decimal fracionado: ")
p = int(input("Insira o número de algorismos no número acima: "))

print(float_bin(n, places=p))

############Atividade5###############

# Converter de octal para binário
def octal_to_binary(octal):
    binary = ""
    for digit in octal:
        binary += format(int(digit), '03b')
    return binary

# Converter de binário para octal
def binary_to_octal(binary):
    octal = ""
    while len(binary) % 3 != 0:
        binary = "0" + binary
    for i in range(0, len(binary), 3):
        octal += str(int(binary[i:i+3], 2))
    return octal

# Converter de hexadecimal para binário 
def hex_to_binary(hexadecimal):
    binary = ""
    for digit in hexadecimal:
        binary += format(int(digit, 16), '04b')
    return binary

# Converter de binário para hexadecimal
def binary_to_hex(binary):
    hexa = ""
    while len(binary) % 4 != 0:
        binary = "0" + binary
    for i in range(0, len(binary), 4):
        hexa += hex(int(binary[i:i+4], 2))[2:]
    return hexa.upper()

# Converter de binário para decimal
def binary_to_decimal(binary):
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[i]) * 2 ** (len(binary) - 1 - i)
    return decimal

# Converter de decimal para binário 
def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

#############ProgramaPrincipal###########
while True:
    print("1. Octal para binário")
    print("2. Binário para octal")
    print("3. Hexadecimal para binário")
    print("4. Binário para hexadecimal")
    print("5. Binário para decimal")
    print("6. Decimal para binário")
    print("7. Sair")
    choice = input("Insira sua escolha: ")
    if choice == "1":
        octal = input("Insira um número octal: ")
        binary = octal_to_binary(octal)
        print("Binário equivalente:", binary)
    elif choice == "2":
        binary = input("Insira um número binário: ")
        octal = binary_to_octal(binary)
        print("Octal equivalente:", octal)
    elif choice == "3":
        hexa = input("Insira um número hexadecimal: ")
        binary = hex_to_binary(hexa)
        print("Binary equivalente:", binary)
    elif choice == "4":
        binary = input("Insira um número binário: ")
        hexa = binary_to_hex(binary)
        print("Hexadecimal equivalente:", hexa)
    elif choice == "5":
        binary = input("Insira um número binário: ")
        decimal = binary_to_decimal(binary)
        print("Decimal equivalente:", decimal)
    elif choice == "6":
        decimal = int(input("Insira um número decimal: "))
        binary = decimal_to_binary(decimal)
        print("Binário equivalente:", binary)
    elif choice == "7":
        break
    else:
        print("Escolha Inválida")


