import time , os , random

def draw_board(spots):
    board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
             f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
             f"|{spots[7]}|{spots[8]}|{spots[9]}|")
    print(board)

def editorial_p(devMode):
    #Choose the type of match
    if devMode == False:
            os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome to the Tic Tac Toe game!")
    print("The game is built and developed by E477")
    print("     X     |     O     |     X     ")
    print("-----------+-----------+-----------")
    print("     O     |     X     |     O     ")
    print("-----------+-----------+-----------")
    print("     X     |     O     |     X     ")
    print("Choose the type of match you want.")
    print("1. Bot")
    print("2. PVP")
    play_with_bot = True if int(input()) == 1 else False
    return play_with_bot

def expect_the_best_choice(spots,type_tag):
    winning_models = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    looping = True
    loopIndex = 0
    cstp = -1
    while looping:
        v1 = spots[winning_models[loopIndex][0]]
        v2 = spots[winning_models[loopIndex][1]]
        v3 = spots[winning_models[loopIndex][2]]
        loopIndex = loopIndex + 1

        if v1 == v2 == type_tag and v3.isnumeric():
            cstp = v3
            looping = False
        elif v1 == v3 == type_tag and v2.isnumeric():
            cstp = v2
            looping = False
        elif v2 == v3 == type_tag and v1.isnumeric():
            cstp = v1
            looping = False
        if loopIndex + 1 == len(winning_models):
            looping = False
    return cstp

def bot_turn(spots ,turn,devMode):
    if devMode == False:
        os.system('cls' if os.name == 'nt' else 'clear')

    draw_board(spots)
    print("It's the bot turn, he's thinking, wait a bit.")

    #Check for a threat
    cstp = expect_the_best_choice(spots,check_turn(turn))

    if cstp == -1:
        cstp = expect_the_best_choice(spots,check_turn(turn + 1))

    if cstp != -1 :
        spots[int(cstp)] = check_turn(turn)
    else:
        fp = []
        for i in spots:
            spotVal = spots[i]
            try:
                fp.insert(1,int(spotVal))
            except:
                pass
        spots[random.choice(fp)] = check_turn(turn)
    time.sleep(2)



def check_turn(turn):
    if turn % 2 == 0:
        return 'X'
    else:
        return 'O'

def check_for_win(spots):
    c1 = (spots[1] == spots[2] == spots[3]) \
            or (spots[4] == spots[5] == spots[6]) \
            or (spots[7] == spots[8] == spots[9])
    c2 = (spots[1] == spots[4] == spots[7]) \
            or (spots[2] == spots[5] == spots[8]) \
            or (spots[3] == spots[6] == spots[9])
    
    c3 = (spots[1] == spots[5] == spots[9]) \
            or (spots[3] == spots[5] == spots[7])
    

    if c1 or c2 or c3 : 
        return True
    else:
        return False
