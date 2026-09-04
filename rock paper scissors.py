import random
print("Lets play rock,paper,scissors")
user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]
while True:
    user_input = input("Enter rock, paper, scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        print("Invalid choice! Try again.")
        continue
    random_number = random.randint(0,2)
    computer_pick=options[random_number]
    computer_pick = random.choice(options)
    print(f"Computer picked: {computer_pick}")
    if user_input == computer_pick:
        print("It's a tie!")
    elif (user_input == "rock" and computer_pick == "scissors") or \
         (user_input == "paper" and computer_pick == "rock") or \
         (user_input == "scissors" and computer_pick == "paper"):
        print("You win!")
        user_wins += 1
    else:
        print("You lose!")
        computer_wins += 1
print(f"\nFinal Score — You_wins: {user_wins}, Computer_wins: {computer_wins}")
print("Thanks for playing!")
