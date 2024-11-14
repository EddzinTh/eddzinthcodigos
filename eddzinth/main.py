# aqui o sistema pede o nokme do usuario 
Nome = input("Digite seu nome;")
#aqui o sistema pede a idade do usuario
idade = int(input("qual a sua idade"))

# aqui mostra o nome e a idade que o usuario informou
print(f"bem vindo{Nome}, voce tem{idade}anos")

#aqui é uma função que serve como menu
def menu():
    print("como posso te ajudar")

    print("1-bebidas")
    print("2-salgados")
    print("3-doces")

    opc_user = int(input("digite o numero da opção desejada"))

#aqui começa a logica
    if opc_user ==1:
        print("temos coca, fanta e guaraná")

    elif opc_user ==2:
        print("temos, coxinha, risolhes e empadinha")

    elif opc_user ==3:
        print("temos brigadeiro")
        
    else:
        print("opção incorreta digite um numero de 1 a 3")

    menu()
