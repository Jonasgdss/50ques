id=int(input('Quantos anos voce tem?'))
cnh=input(str('Voce tem CNH?(sim/Não)')).strip().lower()
if id  >= 18 and cnh =='sim':
    print('Voce é apto a dirigir')
else:
    print('Voce não pode dirigir')