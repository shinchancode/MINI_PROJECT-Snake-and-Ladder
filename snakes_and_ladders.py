
# AARTI RATHI
# My website - https://aartirathi17.herokuapp.com/
#snakes and ladders
#-----------------------------------------------------------------------------------------------------------------
import random

def create_board(players):
    board = [] # a list (dynamic array)
    for i in range(100): #0-99
        element = [i+1, [' ']*players , ' '] # [number, pegs[], sym]
        board.append(element)
    return board

def display_board(board):
    print()
    i, x, flag = 1, 99, 0

    while i <=10:
        print() #row change : rendered by bringing cursor on the next line
        j = 1
        while j <= 10:
            # element printing
            print(board[x], end= ' ')
            x = x -1 if flag == 0 else x+1  #var = valOnTrue if condn else valOnFalse
            j+=1

        x = x -9 if flag == 0 else x - 11
        flag = (flag+1)%2
        i+=1
    print()


def dice(isBot=False):
    totVal = 0
    for i in range(3): #max 3 chances
        #rendering
        if not isBot:
            if i == 0:
                _ = input('Press enter to dice')
            else:
                _ = input('Redice as you got 6')
        else:
            if i == 0:
                print('Bot dices ')
            else:
                print('Bot redices as it got 6 ')

        #dicing logic
        currVal = random.randint(1,6) # a random value in range 1-6
        totVal += currVal
        if currVal != 6:
            break
    return totVal % 18


def snakes_and_ladders(): #GAME
    #how many players?
    playerCount = int(input('Enter the number players (1-4) '))

    #validation
    if playerCount < 1 or playerCount > 4:
        print('Invalid Player Count')
        return

    #bot option
    botPlaying = False #flag
    if playerCount < 4:
        ch = input('Do you want to play with the System? (y/n) ')
        if ch == 'y' or ch == 'Y':
            botPlaying = True
            playerCount+=1

    #define the board
    board = create_board(playerCount)

    #define the players
    players_symbols = [] #sym1(♥), sym2 (♦), ...
    players_score = []

    # distribute the pegs
    pegs = ['♥','♦','♣','♠'] #Alt+3, Alt+4, Alt+5, Alt+6

    for i in range(playerCount): #for playerCount number of times
        players_symbols.append(pegs[i])
        players_score.append(-1) #to ensure that default loc is behind value 1, 0 is the index of value 1

    #lets play
    current = 0
    rank = 1
    while playerCount > 1:
        print(players_symbols[current], 'plays ')
        diceValue = dice(current == playerCount-1 and botPlaying)
        print(players_symbols[current], 'got', diceValue)


        if players_score[current] + diceValue > 99: #value 100
            print('Chance void')
            print(players_symbols[current], 'needs', 99- players_score[current])
        #elif board[players_score[current] + diceValue] == 'SNAKE HEAD':
        #    #erase the peg from original position
        #    board[players_score[current]][1][current] = ' '
        #    #apply the diceValue to the score
        #    players_score[current] = POS SNAKE TAIL
        #    #draw the peg at new position
        #    board[players_score[current]][1][current]= players_symbols[current]
        #elif board[players_score[current] + diceValue] == 'LADDER HEAD':
        #    #erase the peg from original position
        #    board[players_score[current]][1][current] = ' '
        #    #apply the diceValue to the score
        #    players_score[current] = POS LADDER TAIL
        #    #draw the peg at new position
        #    board[players_score[current]][1][current]= players_symbols[current]

        else:
            #erase the peg from original position
            board[players_score[current]][1][current] = ' '
            #apply the diceValue to the score
            players_score[current] += diceValue
            #draw the peg at new position
            board[players_score[current]][1][current]= players_symbols[current]

            #render
            display_board(board)

        #winning
        if players_score[current] == 99: #value 100
            if current == playerCount -1: #bot
                botPlaying = False

            print(players_symbols[current], 'WINS !!!')
            print('Rank: ', rank)
            rank+=1
            #remove the player
            players_symbols.pop(current)
            players_score.pop(current)
            #reduce the player count
            playerCount-=1

        #change the player
        current = (current+1) % playerCount

    print(players_symbols[0], 'LOSES!!!')

def main():
    snakes_and_ladders()

main()
#----------------------------------------------------------------------------------------------------------------