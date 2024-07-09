import random
print("Rock Paper Scissors!")
def play():
    while True:
        you = input("Enter your choice: rock, paper, scissors or 'quit' ")
        if you == 'quit':
            print("Thank you")
            break
        computer = random.choice(['rock', 'paper', 'scissors'])
        print(f"\nYour choice: {you}")
        print(f"Computer's choice: {computer}")

        if you == computer:
            print("It's a tie!")
        elif (you == 'rock' and computer == 'scissors')or(you == 'scissors' and computer == 'paper') or(you == 'paper' and computer == 'rock'):
            print("You win!")
        else:
            print("Computer Wins!")
play()
