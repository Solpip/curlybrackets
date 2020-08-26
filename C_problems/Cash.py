def change():

    cents = 0
    coins = 0

    Change_owed = input("Change owed: ")
    dollars = float(Change_owed)
    cents = round(dollars * 100)

    
    while (cents >= 25):
        cents = cents - 25
        coins = coins + 1
    
    
    while (cents >= 10 and cents < 25):
        cents = cents - 10
        coins = coins + 1
    
        
        
    while (cents >= 5 and cents < 10):
        cents = cents - 5
        coins = coins + 1
    
        
    while (cents >= 1 and cents < 5):
        cents = cents - 1
        coins = coins + 1


    

    print(coins)


change()