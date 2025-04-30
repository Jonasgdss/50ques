n= int(input('Digite um numero:'))
if n %3==0 and n% 5==0:
    print(f'O numero {n} é multiplo de 3 e de 5.')
elif n %3==0:
    print(f'O numero {n} é multuplo apenas de 3.')
elif n%5==0:
    print(f'O numero {n} é multiplo apenas de 5')
else:
    print(f'O numero {n} não é multiplo de 3 nem de 5.')
