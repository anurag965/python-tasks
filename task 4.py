import random

while True:
    user_score=0
    comp_score=0
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    
    print("User's turn...")
    choice = int(input("Enter your choice number from the above line :"))
    if choice == 1:
        user_choice = 'Rock'
    elif choice == 2:
        user_choice = 'Paper'
    else:
        user_choice = 'Scissors'
    print('User choice is: ', user_choice)
    
    print("Computer's Turn....")
    comp_choice = random.randint(1, 3)
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = 'RocK'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'
    print("Computer choice is: ", comp_choice_name)
    
    if choice == comp_choice:
        print('Its Draw', end="")
        result = "DRAW"
        
    if (choice == 1 and comp_choice == 2):
        print('paper wins', end="")
        result = 'Paper'
        
    elif (choice == 2 and comp_choice == 1):
        print('paper wins', end="")
        result = 'Paper'
        
    if (choice == 1 and comp_choice == 3):
        print('Rock wins\n', end="")
        result = 'Rock'
        
    elif (choice == 3 and comp_choice == 1):
        print('Rock wins\n', end="")
        result = 'RocK'
    
    if (choice == 2 and comp_choice == 3):
        print('Scissors wins', end="")
        result = 'Scissors'
        
    elif (choice == 3 and comp_choice == 2):
        print('Scissors wins', end="")
        result = 'Rock'
        
    if result == 'DRAW':
        print("\n Its a tie")
        print("User score: ",user_score)
        print("Comp_score: ",comp_choice)
        
    if result == user_choice:
        print("\n User wins")
        user_score+=1
        print("User score: ",user_score)
        print("Comp_score: ",comp_choice)
    else:
        print("\n Computer wins")
        comp_score+=1
        print("User score: ",user_score)
        print("Comp_score: ",comp_choice)
        
    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break

print("thanks for playing")
