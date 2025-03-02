print("""Welcome to Treasure Island.
      Your mission is to find the treasure.
      """)
direction = {"left", "right"}
MESSAGE = ""
choice = input(
    "You're at cross the road. Where do you want to go? Type \"left\" or \"right\" ").lower()

if choice == "right":
    MESSAGE = "You fill into a hole. Game Over"

if choice == "left":
    print("You've come to the lake. there is an island in the middle of lake: ")
    choice = input(
        "type \"wait\" to wait for a boat. Type \"swim\" to swim across. ").lower()

if choice == "swim":
    MESSAGE = "You get attacked by an angry trout. Game Over"

if choice == "wait":
    color_door = input("""You arrive at the island unharmed. there is a house with 3 doors.
                 One red, one yellow and one blue. Witch colour do you choose """).lower()
    if color_door == "blue":
        MESSAGE = "You enter a room of beasts. Game Over"
    elif color_door == "red":
        MESSAGE = "It's a room full of fire. Game Over."
    else:
        MESSAGE = "You found the treasure! You Win"

print(MESSAGE)
