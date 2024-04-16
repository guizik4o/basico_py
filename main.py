# Descobrir se o numero é par/impar
numero = 9

if numero % 2 == 0:
  print ("o numero", numero, "é par")
  print ("fim do programa")
else:
  print ("o numero", numero, "é impar")
  print ("tchau")
  
print ()

# Descobrir se o numero é positivo/negativo/neutro
n = 0

if n > 0:
  print ("o numero", n, "é positivo")
elif n < 0:
  print ("o numero", n, "é negativo")
else:
  print ("o numero", n, "é neutro")
print ("Fim fo programa")

print ()

# Descobrir o meu IMC
idade = 19
peso = 68
altura = 1.55

print ("tenho", idade, "anos", "peso", peso, "kg", "e tenho", altura, "cm de altura")
print  ("IMC =", peso/altura**2,)

print ()

# Classificando o IMC
IMC = 28

if IMC < 18.5:
  print ("seu IMC é", IMC, "você esta abaixo do peso")
elif 18.5 <= IMC < 25:
  print ("seu IMC é", IMC, "você esta com peso normal")
elif 25 <= IMC < 30:
  print ("seu IMC é", IMC, "você esta com sobrepeso")
elif IMC > 30:
  print ("seu IMC é", IMC, "você esta obeso")

print ()

# Descobrindo se o ano é bissexto 
ano = 232
if ano < 1 or ano > 3000:
  print ("ano invalido")
elif ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
  print ("ano bissexto")
else:
  print ("não é bissexto")