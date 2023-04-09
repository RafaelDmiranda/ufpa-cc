#!/usr/bin/env python
# coding: utf-8

# Pegar os números binários e de bits
input_values1 = input("Insira um número binário: ")
input_values2 = input("Insira outro número binário: ")
num_bits = max(len(input_values1), len(input_values2))
# Converter para a representação em complemento de 2
input_values1 = ((1 << num_bits) + int(input_values1, 2)) & ((1 << num_bits) - 1)
input_values2 = ((1 << num_bits) + int(input_values2, 2)) & ((1 << num_bits) - 1)

# Calcular a subtração binaria usando complemento de 2
result = input_values1 + (-input_values2)

# Converter o número binário e mostra-lo
result_bin = bin(result & ((1 << num_bits) - 1))[2:].zfill(num_bits)
print(result_bin)

