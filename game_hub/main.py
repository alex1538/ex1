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