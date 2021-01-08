szam = 1
while szam <= 20:
    szam = szam + 1
    
    import random
    random_szam = random.randint(1,12)
    oszthato3 = ( random_szam % 3 == 0 )
    if oszthato3:
        print(random_szam)
    
        
    