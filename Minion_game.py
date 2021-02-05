##Kevin and Stuart want to play the 'The Minion Game'.


def minion_game(string):
    # your code goes here
    # The Minion Game in Python - Hacker Rank Solution START
    player1 = 0
    player2 =0
    vowels = 'AEIOU'
    leng = len(string)
    for i in range(leng):
        if string[i] in vowels:
            player1 += leng-i
            
        else:
            player2 += leng-i
        
    if player1>player2:
        print("Kevin", player1)
    elif player1<player2:
        print("Stuart", player2)
    else:
        print("Draw")
        
    # The Minion Game in Python - Hacker Rank Solution END


if __name__ == '__main__':
    s = input()
    minion_game(s)
