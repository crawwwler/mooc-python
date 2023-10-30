import random

def roll(die: str):
    a = [3,3,3,3,3,6]
    b = [2,2,2,5,5,5]
    c = [1,4,4,4,4,4]

    if die == "A" :
        return random.choice(a)
    elif die == "B" :
        return random.choice(b)
    elif die == "C" :
        return random.choice(c)
    

def play(die1: str, die2: str, times: int):
    player1 = 0
    player2 = 0
    draw = 0
    for i in range(times):
        x = roll(die1)
        y = roll(die2)
        if x > y :
            player1 += 1
        elif x < y :
            player2 += 1
        else :
            draw += 1
        
        
    return (player1, player2, draw)




if __name__ == "__main__" :
    print(play("A", "B", 100))

