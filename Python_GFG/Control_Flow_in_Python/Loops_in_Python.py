# # 1. Basic While Loop:
# # Simple while loop that counts from 1 to 5
# count = 1
# while count <= 5:
#     print(count)
#     count += 1

# # 2. Infinite Loop with User Input:
# # Infinite loop that exits on user input
# while True:
#     user_input = input("Enter 'quit' to exit: ")
#     if user_input == 'quit':
#         break

# # 3. Loop Control Statements (break and continue):
# # Using break to exit a loop prematurely
# number = 1
# while number <= 5:
#     if number == 3:
#         break
#     print(number)
#     number += 1

# # 4.Using continue to skip an iteration
# number = 0
# while number < 5:
#     number += 1
#     if number == 3:
#         continue
#     print(number)
# # 5.Nested While Loops:

# outer_loop = 1
# while outer_loop <= 3:
#     inner_loop = 1
#     while inner_loop <= 2:
#         print(f"Outer: {outer_loop}, Inner: {inner_loop}")
#         inner_loop += 1
#     outer_loop += 1

# # 6.Using a While Loop with Lists:
# # Iterating through a list using a while loop
# fruits = ['apple', 'banana', 'cherry', 'date']
# index = 0
# while index < len(fruits):
#     print(fruits[index])
#     index += 1

# # 7. User Input with while Loop:
# user_input = ""
# while user_input != "quit":
#     user_input = input("Enter 'quit' to exit: ")
#     print("You entered:", user_input)

# # 8.Loop with break and continue:
# count = 1
# while count <= 5:
#     if count == 3:
#         count += 1
#         continue  # Skip printing 3
#     if count == 5:
#         break  # Exit the loop when count reaches 5
#     print(count)
#     count += 1

# # 9.Using a while loop for Input Validation:
# while True:
#     try:
#         num = int(input("Enter a number: "))
#         break  # Exit the loop if the input is a valid integer
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")

# # 10.Handling Multiple Conditions in a while loop:
# count = 0
# sum_numbers = 0
# while count < 5 and sum_numbers < 20:
#     num = int(input("Enter a number: "))
#     sum_numbers += num
#     count += 1
# print(f"Sum of {count} numbers is {sum_numbers}")

# # 11. Implementing a Countdown Timer:
# import time

# seconds = 10
# while seconds > 0:
#     print(f"Time left: {seconds} seconds")
#     time.sleep(1)  # Pause for 1 second
#     seconds -= 1
# print("Time's up!")

# # 12. Using a while loop for Menu Selection:
# while True:
#     print("Menu:")
#     print("1. Option 1")
#     print("2. Option 2")
#     print("3. Quit")
    
#     choice = input("Enter your choice: ")
    
#     if choice == "1":
#         print("You selected Option 1")
#     elif choice == "2":
#         print("You selected Option 2")
#     elif choice == "3":
#         print("Exiting the menu.")
#         break  # Exit the loop if the user selects '3'
#     else:
#         print("Invalid choice. Please try again.")

# # 13.  Simulating a Game Loop:
# game_over = False
# score = 0

# while not game_over:
#     # Game logic here...
#     user_input = input("Do you want to continue (yes/no)? ")
#     if user_input.lower() == "no":
#         game_over = True

# print(f"Game over! Your final score is {score}")

# # 14. Using a while Loop for Dynamic List Creation:
# my_list = []

# while True:
#     item = input("Enter an item to add to the list (or 'done' to finish): ")
#     if item.lower() == "done":
#         break
#     my_list.append(item)

# print("Your list:", my_list)

# # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# import random

# # Initialize player stats
# player_name = input("Enter your character's name: ")
# player_health = 100
# player_attack = 10
# player_inventory = []

# # Initialize game variables
# rooms = ["Forest", "Cave", "Castle"]
# current_room = random.choice(rooms)
# enemy_health = random.randint(20, 50)
# items = ["Health Potion", "Sword", "Shield"]

# # Game loop
# while player_health > 0:
#     print(f"\n{player_name}'s Stats:")
#     print(f"Health: {player_health}")
#     print(f"Attack: {player_attack}")
#     print(f"Inventory: {', '.join(player_inventory)}")
#     print(f"Current Room: {current_room}\n")

#     # Player options
#     print("Options:")
#     print("1. Explore")
#     print("2. Attack")
#     print("3. Use Item")
#     print("4. Quit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         # Explore a new room
#         current_room = random.choice(rooms)
#         print(f"You entered the {current_room}.")

#         # Encounter enemy
#         if current_room != "Forest":
#             print("An enemy appears!")
#             while enemy_health > 0:
#                 print(f"Enemy's Health: {enemy_health}")
#                 print(f"{player_name}'s Health: {player_health}")
#                 print("Options:")
#                 print("1. Attack")
#                 print("2. Run")
#                 enemy_choice = input("Enter your choice: ")

#                 if enemy_choice == "1":
#                     # Player attacks enemy
#                     damage_dealt = random.randint(0, player_attack)
#                     damage_taken = random.randint(0, 10)
#                     enemy_health -= damage_dealt
#                     player_health -= damage_taken
#                     print(f"You dealt {damage_dealt} damage to the enemy.")
#                     print(f"The enemy dealt {damage_taken} damage to you.")

#                     if enemy_health <= 0:
#                         print("You defeated the enemy!")
#                         player_inventory.append(random.choice(items))
#                         break
#                 elif enemy_choice == "2":
#                     print("You ran away from the enemy.")
#                     break
#         else:
#             print("You find nothing of interest in the forest.")

#     elif choice == "2":
#         # Attack
#         if current_room != "Forest":
#             print("There's no enemy to attack here.")
#         else:
#             print("You can't attack in the forest. Try exploring a different room.")

#     elif choice == "3":
#         # Use Item
#         if player_inventory:
#             print("Inventory:")
#             for index, item in enumerate(player_inventory, start=1):
#                 print(f"{index}. {item}")
#             item_choice = int(input("Enter the number of the item to use: "))
#             if 1 <= item_choice <= len(player_inventory):
#                 used_item = player_inventory.pop(item_choice - 1)
#                 player_health += random.randint(10, 30)
#                 print(f"You used {used_item} and gained health.")
#             else:
#                 print("Invalid item choice.")
#         else:
#             print("Your inventory is empty.")

#     elif choice == "4":
#         print("Thanks for playing!")
#         break

#     else:
#         print("Invalid choice. Try again.")

#     # Check if the player's health is zero or below
#     if player_health <= 0:
#         print("Game Over! Your character has been defeated.")

# # '''''''''''''''''''''''''''''''''''''''''''''''''''''''
# import random

# # Define the player's attributes
# player_name = input("Enter your name: ")
# player_health = 100
# player_gold = 0

# # Define the game variables
# room_number = 1

# # Main game loop
# while player_health > 0:
#     print(f"\n----- Room {room_number} -----")
    
#     # Generate a random event: monster, treasure, or exit
#     event = random.choice(["monster", "treasure", "exit"])
    
#     if event == "monster":
#         monster_health = random.randint(50, 100)
#         print(f"A wild monster appears with {monster_health} health!")
        
#         while monster_health > 0 and player_health > 0:
#             action = input("Do you want to 'attack' or 'run'?: ")
            
#             if action == "attack":
#                 player_damage = random.randint(10, 30)
#                 monster_damage = random.randint(5, 20)
#                 monster_health -= player_damage
#                 player_health -= monster_damage
#                 print(f"You attack the monster for {player_damage} damage.")
#                 print(f"The monster attacks you for {monster_damage} damage.")
#             elif action == "run":
#                 print("You run away from the monster.")
#                 break
#             else:
#                 print("Invalid action. Choose 'attack' or 'run'.")
        
#         if player_health <= 0:
#             print(f"{player_name} was defeated by the monster. Game over!")
#             break
#         else:
#             print(f"{player_name} defeated the monster and found 50 gold!")
#             player_gold += 50
    
#     elif event == "treasure":
#         found_gold = random.randint(10, 30)
#         print(f"You found a chest with {found_gold} gold!")
#         player_gold += found_gold
    
#     else:
#         print("You found the exit of the dungeon!")
#         print(f"{player_name} successfully escaped with {player_gold} gold!")
#         break
    
#     room_number += 1

# print("Thanks for playing!")

# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# # '''''''''''''''''''''while loop''''''''''''''''''''''
# # Get the number of Fibonacci terms to generate
# num_terms = int(input("Enter the number of Fibonacci terms to generate: "))

# # Initialize variables for the first two Fibonacci numbers
# first_term = 0
# second_term = 1

# # Counter for the number of terms generated
# count = 0

# # Create a list to store the Fibonacci sequence
# fib_sequence = []

# # Start the while loop
# while count < num_terms:
#     # Append the current Fibonacci term to the list
#     fib_sequence.append(first_term)
    
#     # Calculate the next Fibonacci term
#     next_term = first_term + second_term
    
#     # Update the first and second terms
#     first_term = second_term
#     second_term = next_term
    
#     # Increment the counter
#     count += 1

# # Print the generated Fibonacci sequence
# print("Fibonacci Sequence:")
# for term in fib_sequence:
#     print(term, end=" ")

# print()  # Print a newline
