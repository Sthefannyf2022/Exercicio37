 casa = float(input('Digite o valor da casa pretendida'))
salario = float(input('Digite o seu salário atual'))
vezes =  int(input('Quantas vezes pretende pagar'))
v_parcela = casa/vezes
if v_parcela < (salario*0.30):
   print('Para pagar uma casa de R$ {} em {} anos'.format(casa,(vezes /12)))
   print('A prestação sera de {:.2f}'.format(v_parcela))
   print('O emprestimo pode ser concedido')
else:
   print('O valor da parcela {:.2f} excede 30% do seu salario'.format(v_parcela))
   print('O financiamento foi negado')

