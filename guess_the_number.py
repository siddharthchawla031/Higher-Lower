import random
def play_game():

    secret_number=random.randint(1,100)
    print("""_______               ___.                    ________                            .__                   ________                       
     \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____  
     /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ 
    /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/ 
    \____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >
            \/            \/    \/     \/                \/            \/     \/     \/        \//_____/           \/     \/      \/     \/ """)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    choice=input("Choose a difficulty. Type 'easy' or 'hard':")
    if choice=="easy":
        attempts=10
    elif choice=="hard":
        attempts=5
    else:
        print("Invalid choice. Defaulting it to Hard mode. ")
        attempts=5

    while attempts > 0:
        try:
            guess=int(input(f"You have {attempts} attempts remaining. Guess the number between 1 and 100: "))
            if 1 > guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            if guess<secret_number:
                print("Your guess is too low.")
            elif guess>secret_number:
                print("Your guess is too high.")
            else:
                print("You got it!")
                break

            attempts-=1

            if attempts==0:
                print(f"You're out of attempts. The number was {secret_number}. Better luck next time.")
        except:
            print("Sorry, you didn't enter a number. Please try again.")

while True:
    play_game()
    replay=input("Do you want to play again? (y/n): ")
    if replay!="y":
        print("Thank you for playing!")
        break



