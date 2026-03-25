while True: 
    numero = int(input(f"insira um numero para ver sua tabuada :"))
    if numero > 10: 
        print(f"erro")
        continue
    print(f" \na tabuada do{numero}é : \n ")

    for i in range(0, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")