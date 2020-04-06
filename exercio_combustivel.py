qtd= float(input("Digite Quantidade de Combustivel: "))
tipo= input ("Digite o tipo de Combustível: ")

if tipo=="a":
     total = 3.8997 * qtd
     print ("Total de Alcool", total)
elif tipo=="d":
     total = 3.6543 * qtd
     print ("Total de Diesel", total)
elif tipo=="g":
     total= 4.4009 * qtd
     print ("Total de Gasolina", total)
else:
     print ("Combustivel Invalido")

