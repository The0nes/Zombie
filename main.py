import random

def zombie(looting):
    
    num = random.randrange(1, 1000)
    if looting == 0:    
        if num < 25:
            print("Zombie dropped a iron ingot")
        elif num< 50:
            print("Zombie dropped a potato")
        elif num < 75:
             print("Zombie dropped a carrot")    
        else:
            if num<333:
                print("You got 0 rotten flesh")
            elif num <666:
                print("You got 1 rotten flesh")
            else:
                print("You got 2 rotten flesh")

    if looting == 1:
        if num < 35:
            print("Zombie dropped a iron ingot")
        elif num< 60:
            print("Zombie dropped a potato")
        elif num < 85:
            print("Zombie dropped a carrot")
        else:
            if num<333:
                print("You got 0 rotten flesh")
            elif num <666:
                print("You got 1 rotten flesh")
            else:
                print("You got 2 rotten flesh")
              
    if looting == 2:
     
        if num < 45:
            print("Zombie dropped a iron ingot")
        elif num < 70:
            print("Zombie dropped a potato")
        elif num < 95:
            print("Zombie dropped a carrot")
        else:
            if num<333:
                print("You got 0 rotten flesh")
            elif num <666:
                print("You got 1 rotten flesh")
            else:
                print("You got 2 rotten flesh")
             
    if looting == 3:
     
        if num < 55:
            print("Zombie dropped a iron ingot")
        elif num < 80:
            print("Zombie dropped a potato")
        elif num < 105:
            print("Zombie dropped a carrot")
        else:
            if num<333:
                print("You got 0 rotten flesh")
            elif num <666:
                print("You got 1 rotten flesh")
            else:
                print("You got 2 rotten flesh")


    choice = 'a'
    while choice != 'q':
        print("enter looting level, or 'q' to quit")
    choice = input()
    if choice != 'q':
    
        zombie(int(choice))



