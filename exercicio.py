def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  
            else:
                return False  
        else:
            return True  
    else:
        return False  


ano = int(input("Digite um ano: "))
if is_leap_year(ano):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")
