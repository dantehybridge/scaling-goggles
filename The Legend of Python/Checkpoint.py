import random

start_msg = """
================================
Rock Paper Scissors Lizard Spock
================================
The game is an expansion on the game Rock, Paper, Scissors. Each player picks a variable and reveals it at the same time. The winner is the one who defeats the others. In a tie, the process is repeated until a winner is found.
"""

rules_msg = """
================================
Rules for declaring the winner 🏆
================================
-> Scissors cut Paper 
-> Paper covers Rock 
-> Rock crushes Lizard 
-> Lizard poisons Spock
-> Spock smashes Scissors 
-> Scissors beat Lizard 
-> Lizard eats Paper 
-> Paper disproves Spock 
-> Spock vaporizes Rock 
-> Rock breaks Scissors
"""

hands_msg = """
================================
         G A M E    O N
================================
1) ✊ - rock
2) ✋ - paper
3) ✌️ - scissors
4) 🤏 - lizard
5) 🖖 - Spock
"""

print(start_msg, rules_msg, hands_msg)

user_input = int(input("Choose an option: "))
comp_input = random.randint(1, 5)

print(f"User input: {user_input}. Comp input: {comp_input}")

if user_input < 1 or user_input > 5:
    print("Invalid choice. Please choose an option between 1 and 5 to play.")
elif user_input == comp_input:
    print("Oh, no, you are tied! Play again so one can emerge victorious!")
elif (user_input == 1 and (comp_input == 3 or comp_input == 4)) or \
(user_input == 2 and (comp_input == 1 or comp_input == 5)) or \
(user_input == 3 and (comp_input == 2 or comp_input == 4)) or \
(user_input == 4 and (comp_input == 5 or comp_input == 2)) or \
(user_input == 5 and (comp_input == 3 or comp_input == 1)):
    print("""
================================
YOU'RE THE WINNER OF THIS ROUND!
================================
    """)
else:
    print("""
================================
       G A M E    O V E R
================================
    """)