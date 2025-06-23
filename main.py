from art import logo, vs
from game_data import data
import random
print(logo)
sample1 = [1]
sample2 = [1]
score = 0
def who_win(a, b):
    if a[0]['follower_count'] > b[0]['follower_count']:
        return a
    else:
        return b
def pick_two(a, b):
    a[0] = data[random.randint(0,49)]
    b[0] = data[random.randint(0,49)]
    while a == b:
        b[0] = data[random.randint(0, 49)]
    return 0
pick_two(sample1, sample2)
print(f"Compare A: {sample1[0]['name']}, a {sample1[0]['description']}, from {sample1[0]['country']}.\n{vs}\nAgainst B: {sample2[0]['name']}, a {sample2[0]['description']}, from {sample2[0]['country']}.")
player_answer = input('Who has more followers? Type \'A\' or \'B\': ')
answer = {'A':'sample1', 'B':'sample2'}
if answer[player_answer] == who_win(sample1, sample2):
    win_or_lose = True
    score +=1
    print('You\'re right!, Current score: 1.')
else:
    print('Sorry, that\'s wrong. Final score: 0')
    win_or_lose = False
while win_or_lose == True:
    pick_two()
    print(
        f"Compare A: {sample1[0]['name']}, a {sample1[0]['description']}, from {sample1[0]['country']}.\n{vs}\nAgainst B: {sample2[0]['name']}, a {sample2[0]['description']}, from {sample2[0]['country']}.")
    player_answer = input('Who has more followers? Type \'A\' or \'B\': ')
    if answer[player_answer] == who_win(sample1, sample2):
        win_or_lose = True
        score += 1
        print(f'You\'re right!, Current score: {score}.')
    else:
        print(f'Sorry, that\'s wrong. Final score: {score}.')
        win_or_lose = False










