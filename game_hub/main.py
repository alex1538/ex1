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
        user = input("Rock, Paper or Scissors?")
        list_play = ["R", "P", "S"]