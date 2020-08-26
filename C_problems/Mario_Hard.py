Height = input("Height: ")
Height = int(Height)
print("\n")
i = 0


def Func():
    global i, spaces, Height
    if Height > 0 and Height < 9:

        while i < Height:
            
            i += 1

            spaces = (Height - 1) - i

            while spaces >= 0:
                if spaces >= 0:
                    spaces -= 1
                    print(" ", end = '')
                    
            x = 0    

            while x < i:
                x += 1
                print("#", end = '')

            print(" ", end = '')

            y = 0
            
            while y < i:
                y += 1
                print("#", end = '')

            
            print("")


Func()