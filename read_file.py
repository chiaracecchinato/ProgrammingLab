values = [] #lista vuota in cui salvo i valori

my_file=open('shampoo_sales.csv', 'r')

#faccio il for per separare i 2 valori e salvarli in 2 variabili disitinte e poi sommarle in values
for line in my_file:
    elements=line.split(',')

if elements[0] != 'Date':
    date=elements[0]
    value_S=elements[1]

    value_N=float(value_S)

    values.append(float(value_N))

#for i in values:
 #   risu+=i

#def somma():
 #   risu=0
 #  for number in values:
 #     risu+=number
 #return risu
 
print('somma valori tot: ', sum(values))

my_file.close()