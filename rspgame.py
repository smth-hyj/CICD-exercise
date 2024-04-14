import random
def play(): 
    user = input("'r'은 바위 's'은 가위 'p'은 보입니다. 가위바위보를 시작합니다. : ")
    computer = random.choice(['r','s','p'])

    if user == computer:
        return "비겼습니다."

    elif is_win(user, computer):
        return "이겼습니다."
    return "졌습니다."

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return true

print(play())
