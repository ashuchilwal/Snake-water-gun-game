import random
lst = ['s', 'g', 'w']

choice = 5
no_of_chance = 0
com_point = 0
user_point = 0

while no_of_chance < choice:
    user_guess = input("enter your choice :")
    com_out = random.choice(lst)
    if com_out == 's' and user_guess == 's':
        print("same guess ")
        
    elif com_out == 's' and user_guess == 'g':
        print("user win")
        user_point+=1
        
    elif com_out == 's' and user_guess == 'w':
        print("com win")
        com_point+=1
    
    elif com_out == 'g' and user_guess == 's':
        print("com win")
        com_point+=1
        
    elif com_out == 'g' and user_guess == 'g':
        print("same guess")
        
    elif com_out == 'g' and user_guess == 'w':
        print("user win")
        user_point+=1
        
    elif com_out == 'w' and user_guess == 's':
        print("user win")
        user_point+=1
        
    elif com_out == 'w' and user_guess == 'g':
        print("com win")
        com_point+=1
        
    elif com_out == 'w' and user_guess == 'w':
        print("same guess")
        
    else:
        print("wrong input")
        
    no_of_chance = no_of_chance+1
    print(f"{choice-no_of_chance} is left of {choice} \n")
    
print("game over")

if com_point == user_point:
    print("match is drow")
elif com_point > user_point:
    print(f"overall computer win!!! computer point is {com_point} user point is {user_point}")
else:
    print(f"overall user win!!! computer point is {com_point} user point is {user_point}")