import random

start = input("You start game 'Rock Paper Scissors'. For start press '+' and '-' to quit.")

if start == "+":
    print("Loading...")
    print("Game starting!")
    print("3...2...1...Go!")
    print("If you want qiut - press '-'")
    print("If you want known your score - press '?'")
    user_ball = 0
    rand_ball = 0
    while True:
        user = input("Rock - 'R' , Paper - 'P' or Scissors - 'S'?")
        list_play = ["R", "P", "S"]
        if user in list_play:
            rand = random.choice(list_play)
            print(rand)

            if rand == "R" and user == "S":
                rand_ball += 1
            if rand == "S" and user == "P":
                rand_ball += 1
            if rand == "P" and user == "R":
                rand_ball += 1

            if rand == "P" and user == "S":
                user_ball += 1
            if rand == "S" and user == "R":
                user_ball += 1
            if rand == "R" and user == "P":
                user_ball += 1

            if rand == user:
                pass
        elif user == "?":
            print(f"Your score - {user_ball}, score your enemy - {rand_ball}")
        elif user == "-":
            print(f"Your score - {user_ball}, score your enemy - {rand_ball}")
            print("Thank you for game! Have a nice day!")
            break
        else:
            print("Write - R,P or S")

if start == "-":
    print("Very sad! ave a nice day!")
else:
    print("Sorry, I dont understant you. Restasrt a game please.")