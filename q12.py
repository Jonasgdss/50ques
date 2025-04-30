n= int(input('Digite um numero inteiro:'))
if n> 0 and n %2==0:
    print('O numero é positivo e par.')
elif n>0 and n %2 !=0:
    print('O numero é positivo e ímpar.')
elif n<= 0 and n %2==0:
    print('O numero não é positivo mas é par.')
else:
    print ('O numero não é positivo e tambem não é par, ou seja, é negativo e impar.)')
