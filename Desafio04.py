'''Faça um programa em Python que leia algo pelo teclado e mostre na tela 
o seu  tipo primitivo e todas as informações possíveis sobre ela'''
#
digit = input("Digite algo:")
print(digit)
print("Tipo:",type(digit))
print("Alphanumerico:",digit.isalnum())
print("Alfabético:",digit.isalpha())
print("Decimal:",digit.isdecimal())
print("Digito:",digit.isdigit())
print("Minúsculo:",digit.islower())
print("Numérico:",digit.isnumeric())
print("Pode ser impresso:",digit.isprintable())
print("Tem espaços:",digit.isspace())
print("É um titulo:",digit.istitle())
print("Maíusculo:",digit.isupper())
