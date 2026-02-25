nome = (input ("insira um nome "))
idade = int (input ("insira idade( anos completos: "))

#repete quando a idade for valida
while idade > 120 or idade < 0:
 idade = int(input("idade(anos completos -ate 120 ano):"))
 dias_vidas = idade * 36
 print (f"") 