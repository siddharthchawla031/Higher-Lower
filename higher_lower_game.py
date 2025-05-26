from art import logo,vs
from game_data import data
import random as r


data_b = data[r.randint(0, 49)]
score = 0

while True:
    # clear()
    data_a = data_b
    data_b = data[r.randint(0, 49)]
    if data_a == data_b:
        continue
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}.")
    print(f"Compare A: {data_a['name']}, a {data_a['description']}, from {data_a['country']}.  ")
    print(vs)
    print(f"Against B: {data_b['name']}, a {data_b['description']}, from {data_b['country']}.  ")
    user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    if data_a['follower_count'] > data_b['follower_count']:
        right_answer = 'A'
    elif data_a['follower_count'] < data_b['follower_count']:
        right_answer = 'B'
    if user_answer != right_answer:
        break
    else:
        score += 1

# clear()
print(logo)
print(f"Sorry that's wrong, Final score is: {score}\n")
print(
    f"{data_a['name']} has {data_a['follower_count']} million followers,\n while {data_b['name']} has {data_b['follower_count']} million followers")


